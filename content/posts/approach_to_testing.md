Title: An Approach to Python Testing
Author: AC
Date: 2024-03-25
Tags: testing
Slug: approach-to-testing
Summary: Practical testing practices

# TDD? Sort of and not really

I usually work in brand new code or in projects that are still very actively being developed, so it's normal for me to be in situations where we're figuring out exactly what to do and how to do it. I think of writing code as being similar (in some ways) to writing an article or a story: different people will naturally use different approaches to organize their work. 

What I mean by that is that some people are more inclined to outline and others are more inclined to discover their way through a project. Without additional context, I don't think either way is 'better'. I map strict TDD to an outlining approach and the way I tend to do things is closer to a discovery approach. Usually, I work out what I want to do and write a very simple first draft, then I start writing tests, and the tests show me some of the places I did things in a funky way, so I go back and clean those up so that I can test them (and so that my colleagues and I will be able to understand the code later).

## Maximize coverage, minimize time

- Test that the major pieces work together first. I call this 'integration testing', but call it whatever makes sense for your team! The idea is to test the overall functionality of what you've built first, including the expected path through the code and any exceptions that are being handled.

- After that, add tests that exercise smaller portions of the code that weren't touched by the integration tests or that are particularly important.

- It's generally not useful to have a line of code tested multiple times unless it's particularly important. That said, if a line gets tested more than once in the course of writing a small number of tests that are minimally necessary to cover the code, that's fine.

## What's testing good for?

- Proof that the code works as expected.

- Supports extension and refactoring.

    There should be enough coverage that the code can be changed and the tests will still signal whether the change affected something out of scope. The tests should also be general enough that some changes to the code can be made and the tests will still run, which means that tests should mostly focus on the results of the code as opposed to details of the implementation. 
    
    There might be small tests that focus on implementation if something is tricky or crucial, and those tests wouldn't be helpful in assessing refactoring or extension updates if the changes were to affect the lines they test. That doesn't mean those tests have no place, but it does mean that it's important to have some tests that cover that area without being closely coupled to implementation details.

- Additional documentation for how the code should be used.

    This is an easily overlooked function of testing. Tests should be as clear and easy to understand as code, because they will also need maintenance and they have a role in communicating about the code. If tutorials and READMEs explain the goals of the code and how to use it, the tests serve as another source of usage examples.