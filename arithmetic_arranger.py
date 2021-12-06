

def arithmetic_arranger(problems, solution=False):

  arranged_problems = ""

  first_line = []
  second_line = []
  third_line = []
  separator = []

  if len(problems) > 5:  # the problem limit is five (in the rules)
    return "Error: Too many problems."


  for problem in problems:
    operator = ""
    parts = []

    if "+" in problem:
      operator = "+"
    elif "-" in problem:
      operator = "-"
    else:
      return "Error: Operator must be '+' or '-'."
    
    
    parts = problem.split(operator)
    parts = [x.strip() for x in parts]
    
    try:
      partsi = [int(i) for i in parts]
    except:
      return "Error: Numbers must only contain digits."

    for i in partsi:
      if i > 9999:
        return "Error: Numbers cannot be more than four digits."

    if operator == "+":
      parts.append(str(sum(partsi)))
    else:
      parts.append(str(partsi[0] - partsi[1]))

    
    # makes sure all nums are exactly the same length to be printed nicely
    while len(parts[0]) > len(parts[1]):
      parts[1] = " " + parts[1]
    
    while len(parts[0]) < len(parts[1]):
      parts[0] = " " + parts[0]    

    parts[0] = "  " + parts[0]
    parts[1] = operator + " " + parts[1]
        
    while len(parts[2]) < len(parts[1]):
      parts[2] = " " + parts[2]
    
    
    
    first_line.append(parts[0])
    second_line.append(parts[1])
    third_line.append(parts[2])
    separator.append("-" * len(parts[0]))
    

  # print("    ".join(first_line))
  # print("    ".join(second_line))
  # print("    ".join(separator))
  # print("    ".join(third_line))

  arranged_problems += "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(separator)

  if solution:
    arranged_problems += "\n" + "    ".join(third_line)

  return arranged_problems
