# Python implementation of Cellular Automata 
## First Software and Computing Project 2021/2022

Good Morning to everyone! :smile:

The aim of this first Software and Computing for Applied Physics' project is to implement a **simple cellular automata** (based on the rules detailed by *Wolfram*) and to get comfortable with the Git-Hub ambient. The working-team is composed by Lorenzo Barsotti, Daniele Buschi and Keivan Amini.

In this project, the algorithm implemented is the so-called *Rule 30*, for which we can use [Mathworld Wolfram](https://mathworld.wolfram.com/Rule30.html) as a reference. Moreover, the methods used to implement the algorithm are inspired by this [blog](https://faingezicht.com/articles/2017/01/23/wolfram/).



<p align="center">
  <figure>
  <img src="https://mathworld.wolfram.com/images/eps-svg/ElementaryCARule030_1000.svg" />
  <figcaption> Rule 30 specifies the next color in a cell, depending on its color and its immediate neighbors. In this image we can see the evolution of a single black cell it produces after 15 step. </figcaption>
  </figure>
</p>


For the rules detailed by *Wolfram*, the system is represented by a string of 0 and empty spaces that represent alive and dead cells. One of the most important concept is that the evolution is based on the status of each character and its neighbours.
