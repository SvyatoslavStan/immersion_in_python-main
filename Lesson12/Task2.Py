class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __setattr__(self, key, value):
        if key == "name":
            if not value.istitle() or not value.isalpha():
                raise ValueError("Имя должно начинаться с заглавной буквы и состоять только из букв")
        elif key == "age":
            if not isinstance(value, int) or not (0 <= value <= 120):
                raise ValueError("Возраст должен быть целым числом от 0 до 120")
        elif key == "email":
            if "@" not in value:
                raise ValueError("Email должен содержать символ '@'")

        super().__setattr__(key, value)

    def __str__(self):
        return f"Person(name={self.name}, age={self.age}, email={self.email})"



try:
    person = Person("Иван", 30, "ivan@example.com")
    print(person)

    person.age = 25  
    person.email = "new_email@example.com"  
    print(person)

except ValueError as e:
    print(e)
