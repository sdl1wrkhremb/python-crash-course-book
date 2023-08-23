def make_car(manufacturer, model, **options):
    # build a dictionary to store car information
    options['manufacturer'] = manufacturer
    options['model'] = model
    return options


car = make_car('subaru', 'sti', color='blue', tow_package=True, turbo=True)
print(car)
