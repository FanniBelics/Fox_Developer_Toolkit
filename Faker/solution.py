from faker import Faker
from faker.providers import DynamicProvider
from faker_ecommerce import EcommerceProvider

faker = Faker('en_US')
faker.add_provider(EcommerceProvider)

# Foreign keys referencing the country table, Oracle SH schema
country_provider = DynamicProvider(
    provider_name="country_id_provider",
    elements=[52790, 52776, 52789, 52784, 52780, 52777, 52779, 52778, 52788, 52786, 52775, 52773, 52783, 52782, 52781, 52774, 52785, 52791, 52787, 52772, 52771, 52769, 52770]
)
faker.add_provider(country_provider)

def escape_sql_string(value: str | None) -> str:
    """
        Escape single quotes in a string for SQL insertion
        
        Arguments:
            value (str): The string to escape
    """
    
    if value is None:
        return "NULL"
    
    
    return value.replace("'", "''")

def generate_user_inserts(number_of_records: int) -> list[str]:
    """
        Generate SQL insert statements for the Users table
        
        Arguments:
            number_of_records (int): The number of user records to generate
    """
    
    statements = []
    for _ in range(number_of_records):
        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        password = faker.password(length=12)
        created_at = faker.date_time_this_decade()
        
        statement = f"INSERT INTO Users (first_name, last_name, email, password, created_at) VALUES ('{escape_sql_string(first_name)}', '{escape_sql_string(last_name)}', '{escape_sql_string(email)}', '{escape_sql_string(password)}', to_date('{created_at}', 'YYYY-MM-DD HH24:MI:SS'));"
        statements.append(statement)
        
        
    return statements

def generate_product_inserts(number_of_records: int) -> list[str]:
    """
        Generate SQL insert statements for the Products table
        
        Arguments:
            number_of_records (int): The number of product records to generate
    """
    statements = []
    for _ in range(number_of_records):
        product_name = faker.product_name()
        product_description = faker.product_description()
        price = faker.price()
        created_at = faker.date_time_between(start_date='-5y', end_date='now')
        
        statement = f"INSERT INTO Products (product_name, product_description, price, created_at) VALUES ('{escape_sql_string(product_name)}', '{escape_sql_string(product_description)}', {price}, to_date('{created_at}', 'YYYY-MM-DD HH24:MI:SS'));"
        statements.append(statement)
        
    return statements

def generate_address_inserts(number_of_records: int) -> list[str]:
    """
        Generate SQL insert statements for the Addresses table
        
        Arguments:
            number_of_records (int): The number of address records to generate
    """
    statements = []
    for _ in range(number_of_records):
        street = faker.street_address()
        city = faker.city()
        state = faker.state()
        zip_code = faker.zipcode()
        country = faker.country_id_provider()
        created_at = faker.date_time_between(start_date='-5y', end_date='now')

        statement = f"INSERT INTO Addresses (street, city, state, zip_code, country, created_at) VALUES ('{escape_sql_string(street)}', '{escape_sql_string(city)}', '{escape_sql_string(state)}', '{escape_sql_string(zip_code)}', {country}, to_date('{created_at}', 'YYYY-MM-DD HH24:MI:SS'));"
        statements.append(statement)

    return statements

if __name__ == "__main__":
    num_users = 10
    num_products = 10
    num_addresses = 10
    
    user_inserts = generate_user_inserts(num_users)
    product_inserts = generate_product_inserts(num_products)
    address_inserts = generate_address_inserts(num_addresses)
    
    print("User Inserts:")
    for insert in user_inserts:
        print(insert)
        
    print("\nProduct Inserts:")
    for insert in product_inserts:
        print(insert)
        
    print("\nAddress Inserts:")
    for insert in address_inserts:
        print(insert)