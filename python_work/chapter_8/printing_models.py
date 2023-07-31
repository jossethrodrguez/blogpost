def print_models(unprinted_desings, completed_models):
    while unprinted_desings:
        current_desing = unprinted_desings.pop()
        print(f"Printing model: {current_desing}")
        completed_models.append(current_desing)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(f"* {completed_model}")


unprinted_desings = ['phone case', 'robot pedant', 'dodecahedron']
completed_models = []

print_models(unprinted_desings, completed_models)
show_completed_models(completed_models)
