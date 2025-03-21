import prompt_variants
import toetactic
from datasets import Dataset

pv = prompt_variants.get_prompt_variants()

all_states = list(toetactic.generate_data(10000))

#split all states into training and test sets
training_boards = all_states[:230] #2300 prompts for training
test_boards = all_states[230:] #480 prompts for evaluation

training_data = []
eval_data = []

for prompt_variant in pv:
    for board in training_boards:
        strr = prompt_variant[0] + toetactic.print_board(board.game_state) + prompt_variant[1]
        best_move = toetactic.solve_game(board)
        #translate best move to top, center, bottom and left, center, right
        row_names = ["top", "center", "bottom"]
        col_names = ["left", "center", "right"]
        row, col = best_move
        move_str = f"({row_names[row]}, {col_names[col]})"
        strr += move_str
        training_data.append(strr)
    for board in test_boards:
        strr = prompt_variant[0] + toetactic.print_board(board.game_state) + prompt_variant[1]
        best_move = toetactic.solve_game(board)
        #translate best move to top, center, bottom and left, center, right
        row_names = ["top", "center", "bottom"]
        col_names = ["left", "center", "right"]
        row, col = best_move
        move_str = f"({row_names[row]}, {col_names[col]})"
        strr += move_str
        training_data.append(strr)

        eval_data.append(strr)

# Convert lists to datasets
train_dataset = Dataset.from_dict({"text": training_data})
eval_dataset = Dataset.from_dict({"text": eval_data})

# Save datasets to disk
train_dataset.save_to_disk("toetactic_train_dataset")
eval_dataset.save_to_disk("toetactic_eval_dataset")

print(f"Saved {len(training_data)} training examples and {len(eval_data)} evaluation examples to disk.")

