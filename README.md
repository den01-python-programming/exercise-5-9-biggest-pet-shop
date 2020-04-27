# Exercise 5.9 Biggest pet shop

Two classes, `Person` and `Pet`, are included in the exercise template. Each person has one pet. Modify the `__str__` method of the `Person` class so that the string it returns tells the pet's name and breed in addition to the person's own name.

```python
lucy = Pet("Lucy", "golden retriever")
leo = Person("Leo", lucy)

print(leo)
```

```plaintext
Leo, has a friend called Lucy (golden retriever)
```
