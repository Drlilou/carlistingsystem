# seed.py
import os
import shutil
import random
from app import app, db, Car, CarImage  # ← Adjust 'app' if your main file has a different name

# Sample car data
CAR_NAMES = [
    "Toyota Camry", "Honda Civic", "Ford Mustang", "BMW X5", "Mercedes C-Class",
    "Audi A4", "Tesla Model 3", "Hyundai Tucson", "Nissan Altima", "Volkswagen Golf",
    "Chevrolet Malibu", "Kia Sorento", "Subaru Outback", "Mazda CX-5", "Lexus RX"
]

FUEL_TYPES = ["Petrol", "Diesel", "Hybrid", "Electric"]
CAR_TYPES = ["Sedan", "SUV", "Hatchback", "Coupe", "Convertible", "Pickup"]

def clear_existing_data():
    """Delete all cars and images from the database."""
    print("🗑️ Deleting existing cars and images...")
    db.session.query(CarImage).delete()
    db.session.query(Car).delete()
    db.session.commit()
    print("✅ Existing data cleared.")

def ensure_upload_folder():
    """Ensure static/images exists."""
    os.makedirs("static/images", exist_ok=True)

def generate_sample_images():
    """
    Generate or copy sample images to static/images.
    Uses placeholder images if no real images are provided.
    """
    sample_images = []
    for i in range(5):
        filename = f"sample_car_{i+1}.jpg"
        filepath = os.path.join("static/images", filename)
        # Create a simple placeholder image URL (will be downloaded as local file)
        # We'll use picsum.photos (real photos) for better realism
        sample_images.append(filepath)
    return sample_images

def download_image(url, save_path):
    """Download an image from URL and save it."""
    try:
        import requests
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            return True
    except Exception as e:
        print(f"⚠️ Failed to download {url}: {e}")
    return False

def seed_cars():
    """Seed the database with random cars."""
    print("🌱 Seeding cars...")
    
    # Ensure folder exists
    ensure_upload_folder()

    # Prepare local image paths (we'll generate 5 placeholder images)
    local_image_paths = []
    for i in range(5):
        filename = f"local_car_{i+1}.jpg"
        filepath = os.path.join("static/images", filename)
        # Use Picsum Photos (real car-like images)
        img_url = f"https://picsum.photos/600/400?random={i+100}"
        if download_image(img_url, filepath):
            local_image_paths.append(f"images/{filename}")
        else:
            # Fallback to a generic placeholder
            local_image_paths.append("https://placehold.co/600x400/FF8C00/white?text=Car+Image")

    # External image URLs (public, no copyright)
    external_urls = [
        "https://images.unsplash.com/photo-1494976388531-d1058494cdd8?auto=format&fit=crop&w=600",
        "https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=600",
        "https://images.unsplash.com/photo-1493238792000-8113da705763?auto=format&fit=crop&w=600",
        "https://images.unsplash.com/photo-1542362567-b07e54358753?auto=format&fit=crop&w=600",
        "https://images.unsplash.com/photo-1549309002-2d36a49bd837?auto=format&fit=crop&w=600"
    ]

    all_image_sources = local_image_paths + external_urls

    for i in range(10):
        # Random car data
        name = random.choice(CAR_NAMES)
        price = random.randint(80, 300)
        seats = random.choice([2, 4, 5, 7])
        fuel = random.choice(FUEL_TYPES)
        car_type = random.choice(CAR_TYPES)
        description = f"Beautiful {fuel.lower()} {car_type.lower()} perfect for your next adventure."

        # Choose 1–3 random images for this car
        num_images = random.randint(1, 3)
        selected_images = random.sample(all_image_sources, min(num_images, len(all_image_sources)))

        # Create car
        car = Car(
            name=name,
            price_per_day=price,
            seats=seats,
            fuel=fuel,
            car_type=car_type,
            description=description
        )
        db.session.add(car)
        db.session.flush()  # Get car.id

        # Add images
        for img_url in selected_images:
            db.session.add(CarImage(image_url=img_url, car_id=car.id))

        print(f"  ➕ Added: {name} with {len(selected_images)} image(s)")

    db.session.commit()
    print("✅ Database seeded successfully!")

if __name__ == "__main__":
    with app.app_context():
        clear_existing_data()
        seed_cars()