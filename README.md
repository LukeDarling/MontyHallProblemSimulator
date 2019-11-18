## About
I created this small program in order to simulate the statistical outcome of the Monty Hall Problem. I can't fully wrap my head around the math surrounding the Monty Hall Problem, and in fact disagreed with the accepted solution, so I created this program in an attempt to prove the accepted solution to the problem wrong. Ironically, my own program proved myself wrong and proved the accepted solution to be true, leaving me no choice but to accept as truth that which I do not understand.

---
## Information

[Monty Hall Problem on Wikipedia](https://en.wikipedia.org/wiki/Monty_Hall_problem)

---
## Usage

### Ubuntu, Debian Linux

##### Setup

You must first ensure you have the python3 package installed on your system.

```bash
# Update your package repositories
sudo apt update

# Install the most recent version of python3 if it isn't already
sudo apt install python3
```

##### Running

Clone this repo and navigate into the newly created directory for it.

```bash
git clone https://github.com/LukeDarling/MontyHallProblemSimulator.git
cd MontyHallProblemSimulator/
```

Now you can excute the script with the commands below, substituting `<simulations>` for the amount of simulations you wish the script to run and average out.

```bash
python3 mhps.py <simulations>
```

Depending on the amount of simulations you ask the script to do, execution could take a while. When finished, the script will pipe the resulting average to standard output.

Example output:

```
$ python3 mhps.py 100
0.67
$ 
```



### Windows

Might or might not ever bother adding instructions for Windows; it's pretty straightforward, anyway.

---
## Results

The resulting output is analogous to the simulated statistical likelihood of the chosen door being correct if you were to switch doors after the first door's contents are revealed. It makes no sense whatsoever to me that the result is always ~0.66667% instead of what seems like the obvious, logical answer of ~0.5, but the mathematicians seem to have won this round.
