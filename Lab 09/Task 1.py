#Task 1
total_cards = 52
red_cards = 26
hearts = 13
face_cards = 12
diamond_face_cards = 3
spade_face_cards = 3
queens = 4
overlap = 1

p_red = red_cards / total_cards
print("P(Red Card) =", p_red)

p_heart_given_red = hearts / red_cards
print("P(Heart | Red) =", p_heart_given_red)

p_diamond_given_face = diamond_face_cards / face_cards
print("P(Diamond | Face Card) =", p_diamond_given_face)

p_spade_or_queen = (spade_face_cards + queens - overlap) / face_cards
print("P(Spade OR Queen | Face Card) =", p_spade_or_queen)
