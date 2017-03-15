# Useful Enums - a library for creating Enums in a DRY way in Python

This library grew out of me getting fed up with having to create Django
choices that were lists of tuples. I far preferred nicely contained enums of
the form:

    class MyEnum:

        VALUE_1 = 1
        VALUE_2 = 2

However, most of the time you don't _need_ to create all of the IDs yourself.
You should just be able to define the key names and have the Enum class do the
work for you. `usefulenums` does that.

    from usefulenums import Enum

    MyEnum = Enum(
        ("MY_FIRST_VALUE", "My First Display Text"),
        ("MY_SECOND_VALUE", "My Second Value"),
    )
