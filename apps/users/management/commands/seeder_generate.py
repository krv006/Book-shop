from django_seed import Seed
from shops.models import Section, Category
from faker import Faker

faker = Faker()
seeder = Seed.seeder()

seeder.add_entity(Category, 10, {
    'name': lambda x: faker.word(),
})

seeder.add_entity(Section, 10, {
    'name_image': lambda x: faker.image_url(),
    'intro': lambda x: faker.text(),
    'banner': lambda x: faker.image_url(),
})

"""

seeder.add_entity(Section, 10, {
    'name_image': lambda x: faker.image_url(),
    'intro': lambda x: faker.text(),
    'banner': lambda x: faker.image_url(),
})

if __name__ == "__main__":
    seeder.execute()

"""
