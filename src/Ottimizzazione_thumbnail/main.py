from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import Dict, Optional
import base64

class BasicImage:
    """Classe base per simulare un'immagine senza dipendenze esterne"""
    def __init__(self, data: str, width: int, height: int):
        self.data = data
        self.width = width
        self.height = height

    def copy(self):
        return BasicImage(self.data, self.width, self.height)

    def resize(self, new_width: int, new_height: int):
        """Simula il ridimensionamento dell'immagine"""
        self.width = new_width
        self.height = new_height
        # In un caso reale, qui si ridimensionerebbe effettivamente l'immagine
        return self

class IImageService(ABC):
    @abstractmethod
    def get_image(self, image_id: str) -> BasicImage:
        pass

class RealImageService(IImageService):
    def __init__(self, storage_path: str):
        self.storage_path = storage_path

    def get_image(self, image_id: str) -> BasicImage:
        try:
            # Simula il recupero di un'immagine da storage
            # In un caso reale, qui leggeresti effettivamente un file
            dummy_data = f"image_data_{image_id}"
            return BasicImage(dummy_data, 1024, 768)
        except Exception as e:
            raise Exception(f"Errore nel recupero dell'immagine: {str(e)}")

class CachedImage:
    def __init__(self, image: BasicImage):
        self.image = image
        self.last_accessed = datetime.now()

class CacheImageProxy(IImageService):
    def __init__(self, real_service: RealImageService, cache_duration_minutes: int = 20):
        self.real_service = real_service
        self.cache: Dict[str, CachedImage] = {}
        self.cache_duration = timedelta(minutes=cache_duration_minutes)

    def get_image(self, image_id: str) -> BasicImage:
        self._clean_expired_cache()
        
        if self._is_in_cache(image_id):
            return self._get_from_cache(image_id)
        
        image = self.real_service.get_image(image_id)
        self._add_to_cache(image_id, image)
        return image

    def _is_in_cache(self, image_id: str) -> bool:
        return image_id in self.cache

    def _get_from_cache(self, image_id: str) -> BasicImage:
        cached = self.cache[image_id]
        cached.last_accessed = datetime.now()
        return cached.image

    def _add_to_cache(self, image_id: str, image: BasicImage):
        self.cache[image_id] = CachedImage(image)

    def _clean_expired_cache(self):
        current_time = datetime.now()
        expired_keys = [
            key for key, cached in self.cache.items()
            if (current_time - cached.last_accessed) > self.cache_duration
        ]
        for key in expired_keys:
            del self.cache[key]

class ThumbnailProxy(IImageService):
    def __init__(self, cache_proxy: CacheImageProxy, thumbnail_size: tuple = (100, 100)):
        self.cache_proxy = cache_proxy
        self.thumbnail_size = thumbnail_size
        self.thumbnail_cache: Dict[str, BasicImage] = {}

    def get_image(self, image_id: str) -> BasicImage:
        thumbnail_id = f"thumb_{image_id}"
        
        if self._has_thumbnail(thumbnail_id):
            return self._get_thumbnail(thumbnail_id)
        
        original_image = self.cache_proxy.get_image(image_id)
        thumbnail = self._create_thumbnail(original_image)
        self._save_thumbnail(thumbnail_id, thumbnail)
        return thumbnail

    def _has_thumbnail(self, thumbnail_id: str) -> bool:
        return thumbnail_id in self.thumbnail_cache

    def _get_thumbnail(self, thumbnail_id: str) -> BasicImage:
        return self.thumbnail_cache[thumbnail_id]

    def _create_thumbnail(self, image: BasicImage) -> BasicImage:
        thumbnail = image.copy()
        thumbnail.resize(self.thumbnail_size[0], self.thumbnail_size[1])
        return thumbnail

    def _save_thumbnail(self, thumbnail_id: str, thumbnail: BasicImage):
        self.thumbnail_cache[thumbnail_id] = thumbnail

def test_image_system():
    # Inizializzazione dei servizi
    storage_path = "/Thumbnail"
    real_service = RealImageService(storage_path)
    cache_proxy = CacheImageProxy(real_service)
    thumbnail_proxy = ThumbnailProxy(cache_proxy)

    # Test 1: Prima richiesta di un'immagine
    print("\nTest 1: Prima richiesta immagine")
    image_id = "user_123_profile.jpg"
    thumbnail = thumbnail_proxy.get_image(image_id)
    print(f"Immagine originale creata: {thumbnail.data}")
    print(f"Dimensioni thumbnail: {thumbnail.width}x{thumbnail.height}")

    # Test 2: Seconda richiesta della stessa immagine (dovrebbe usare la cache)
    print("\nTest 2: Seconda richiesta della stessa immagine")
    thumbnail2 = thumbnail_proxy.get_image(image_id)
    print(f"Immagine dalla cache: {thumbnail2.data}")
    print(f"Dimensioni thumbnail: {thumbnail2.width}x{thumbnail2.height}")

    # Test 3: Verifica cache
    print("\nTest 3: Verifica stato cache")
    print(f"Immagini in thumbnail cache: {len(thumbnail_proxy.thumbnail_cache)}")
    print(f"Immagini in cache principale: {len(cache_proxy.cache)}")

    # Test 4: Richiesta di un'immagine diversa
    print("\nTest 4: Richiesta nuova immagine")
    new_image_id = "user_456_profile.jpg"
    new_thumbnail = thumbnail_proxy.get_image(new_image_id)
    print(f"Nuova immagine creata: {new_thumbnail.data}")
    print(f"Dimensioni thumbnail: {new_thumbnail.width}x{new_thumbnail.height}")

if __name__ == "__main__":
    test_image_system()