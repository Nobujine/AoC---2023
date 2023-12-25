filename = 'Day 19/input.txt'

with open(filename, 'r') as f:
    workflows, parts = f.read().split('\n\n')

# parse workflows
workflows = workflows.splitlines()
workflow_dict = {}
for w in workflows:
    key, value = w[0:-1].split('{')
    value = value.split(',')
    workflow_dict[key] = value

# Parse parts 
parts = parts.splitlines()
parts = [part[1:-1].split(',') for part in parts]

new_parts = []
for part in parts:
    new_part = {}
    for attribute in part:
        key, value = attribute.split('=')
        new_part[key] = int(value)
    new_parts.append(new_part)
parts = new_parts

def evaluate_workflow(part:dict, workflow:str)->str:
    # returns next workflow to move to
    for step in workflow:
        if ':' not in step:
            return step
        if ':' in step:
            letter = step[0]
            condition = step[1]
            number, next_workflow = step.split(':')
            number = int(number[2:])
            if condition == '<':
                if part[letter] < number:
                    return next_workflow
            if condition == '>':
                if part[letter] > number:
                    return next_workflow
    ...

accepted_parts = []
for part in parts:
    next_workflow = 'in'
    while True:
        next_workflow = evaluate_workflow(part, workflow_dict[next_workflow])
        if next_workflow == 'R':  # Rejected
            break
        if next_workflow == 'A':  # Accepted
            accepted_parts.append(part)
            break
score = sum([sum(part.values())for part in accepted_parts])
print(f'Answer: {score}')
...