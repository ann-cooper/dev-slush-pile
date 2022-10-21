Title: Thinking about debugging
Author: AC
Date: 2022-08-04
Tags: debugging, notes, techniques
Slug: debugging-thinking
Summary: Ways to approach debugging
Status: draft

1. Write down the problem as you understand 
    Don't underestimate the power of communication! Writing helps to focus thinking: this is part of why I often used to find myself answering my own question as soon as I had typed it out in Slack to a colleague.

2. Ask yourself: "How would I write this code if this were the behavior I wanted?"
    I use this technique all the time, in my own projects and talking through projects at work. It doesn't always lead right to the problem, of course, but I've been surprised how often it helps me look in the right direction.

3. Start narrowing down the boundaries of the problem: up to what point are things okay?
    This is usually helpful when the problems are harder to find. The idea is to narrow down where the problem could be as you work. When you start investigating, the boundaries might encompass a whole process that involves several classes. As you continue to work, you can move your boundaries in as you prove to yourself where the code is still performing as expected. For example, if part of the code with a bug involves instantiating an object, you might start by checking that the attributes are all correct on instantiation, then the problem boundary can be moved to after that point in the code, which helps to ensure that you aren't spending time looking into something that's not a problem.

4. Using the pdb
    The built-in Python debugger is very useful. It requires no set up, no special settings in your code editor, and allows you to explore the state of the variables at any point in the code based on where you insert the breakpoint. The way to use it is to put `breakpoint()` in your code at the line where you want to check on the state of things, then run the script, call the method, run the test, etc., when it reaches the breakpoint, it will drop you into the pdb interactive shell, where you can explore things like:
    - The local variables and their values as this point of the code with `locals()`
    - The values of any variable avaialable with pretty print, which is built-in: `pp my_var.__dict__`
    - Step through the code line by line with `n`
    - Run to the next breakpoint with `c`