# C.Cheefoon-ASU-CSE_531-Project_3


## Problem Statement
In the given scenario, N number of Customers and N number of bank Branches; Customer X can submit requests (Deposit, Withdraw or Query) to any branch. It is required that all other Branches be aware of the requests made to keep the balance of all the Branches consistent. In this scenario, the Customer can make requests to any branch making maintaining consistency between branches required. 

## Goal
Using Remote Procedure Call’s communication protocol (more specifically gRPC), design and implement a Distributed System in Python. This system should allow Customers to send requests to any branch of the branch network while remaining consistent. To remain consistent, this project will use the Monotonic Writes and Read Your Writes consistency models. 

## Cool Achievements
 - Wrote the ```server_spawner``` module that handles the creation, port assignment, management, and termination of gPRC server processes.
 - Implemented branch event propagation asynchronously, significantly reducing the time required for event propagation from O(n) to O(1).


## Setup Process

 - Pull the project using git from: https://github.com/CliffordCheefoon/C.Cheefoon-ASU-CSE_531-Project_3.git

 - (Optional) Create a Python virtual environment, and set your terminal to use this environment. Create a venv: ```python3 -m venv .venv```


 - Install the project dependencies using the command :
```pip install -r .\requirements.txt”```

 - (Optional) In the main.py file, there is a configuration variable “TEST_INPUT_FILE”. You can modify this to specify which test case you would like to run. Options include:
   - “tests/monotonic_writes.json” (default)
   - “tests/read_your_writes.json” 

 - Run the program using the command: ```python ./main.py```

 - Observe the terminal debug logs

 - 7.	A file “tests/output/output.json” will be generated with the output. Additionally, each branch server outputs its log stream to its log file located in “tests/server_out/*”. These files are organized by branch_id




