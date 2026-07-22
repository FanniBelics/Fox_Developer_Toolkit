# Faker

Faker is a Python module, that can create you: 
- real-looking data
- localized output — pass a locale like `en_US`, `en_GB`, or `hu_HU` and Faker generates data that matches that region's naming/formatting conventions
- more natural testing

## The problem

Have you ever been in a situation where you needed thousands of records for testing? During my researches I often need real-looking data for testing, something that the database won't cache and something that feels real. 

In this particular case I was stress-testing if an insert trigger in the database affects the database heavily. This is when I found Faker.

## The solution
With faker you can create unique, fake, but real-like data, organized into different categories based on your needs. With faker, I was able to generate thousands of INSERT and UPDATE commands, that could stress-test my triggers with ease.

Here's the core idea — see `solution.py` for the full SQL-generating version:
```
from faker import Faker
from faker.providers import DynamicProvider
from faker_ecommerce import EcommerceProvider

faker = Faker('en_US')
faker.add_provider(EcommerceProvider)

if __name__ == '__main__':
    print(faker.first_name())
    print(faker.last_name())
    print(faker.email())
    print(faker.phone_number())
```

## Setup

To use [Faker](https://faker.readthedocs.io/en/master/) you'll need to install it's module. I advice you to use a *test environment* first, and include Faker in your virtual environments when it's needed.

`pip install faker`

for [commercial data](https://pypi.org/project/faker-ecommerce-provider/)

`pip install faker-ecommerce-provider`

Run the test code

`python solution.py`