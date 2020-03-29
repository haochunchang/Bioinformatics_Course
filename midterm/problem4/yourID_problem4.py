"""
Problem 4 (Optional, 15%)

Description:
Write a class named “Cat” that can perform the following actions:
    .name: print out capitalized name
    .meow(): return the string: “(=^.^=) meow!”
    print(): when print object, print out the string: “My name is [name], I am a cat.”

    Example:
        x = Cat(name=”tom”)
        x.name # print out “Tom” (capitalized name)
        print(x.meow()) # print out “(=^.^=) meow!”
        print(x) # print out “My name is Tom, I am a cat.”
Grading:
    Each action (.name, .meow() and print) gives 5%
"""


class Cat:
    def __init__(self, name):
        pass

    def __str__(self):
        pass

    def meow(self):
        pass


if __name__ == "__main__":
    # Do not modify this part!!!
    # If you change the output format, you may lose you private testing score
    # Since TA use this format to grade the answers
    import sys

    input_path, output_path = sys.argv[1], sys.argv[2]

    with open(input_path, "r") as f, open(output_path, "w") as o:
        for line in f:
            cat_name, ans = line.split("\t")
            x = Cat(name=cat_name)
            your_ans = x.name + "," + x.meow() + "," + str(x) + "\n"
            # Uncomment the following line if you want to check your answers.
            # assert your_ans == ans, "Wrong answer at input#{}".format(i+1)
            o.write(your_ans)
