# Noisy-Text
>Add noise to your text, inspired by [Edunov et al. (2018)](https://arxiv.org/abs/1808.09381) "Understanding Back-Translation at scale"

<p align="center">
  <img src="./animation.gif">
</p>

It is often a good idea to add noise to your syntetic text data, when using backtranslation for example

[Edunov et al. (2018)](https://arxiv.org/abs/1808.09381) showed that doing so can help to provide a stronger training signal


This repository contains:
- A script to reproduce experiments described by [Edunov et al. (2018)](https://arxiv.org/abs/1808.09381) in their noise approach
- A simple architecture so you can play with noise parameters or implement your own noise functions

## Installation

Libraries you'll need to run the project:

{``tqdm``}

Clone the repo using

```sh
git clone https://github.com/valentinmace/noisy-text.git
```

## Usage


## Results
I've implemented the 3 noise functions described in the paper:

- Delete words with given probability (default is 0.1)
- Replace words by a filler token with given probability (default is 0.1)
- Swap words up to a certain range (default range is 3)

The default parameters are to reproduce [Edunov et al. (2018)](https://arxiv.org/abs/1808.09381) experiments but you can play with them and maybe find better values


## Notes

Do not hesitate to contact me if you need some help

Everything is made by me, I did not want to use existing framework for the genetic algorithm or neural network for learning purposes. I also coded the game with performance in mind rather than conception elegance.

I have published (or will publish depending on when you read this) a serie of youtube tutorial videos on [my channel](https://www.youtube.com/channel/UCMIW0JKxoxBDM5yiiF17SrA) (in french)


## Meta

Valentin Macé – [LinkedIn](https://www.linkedin.com/in/valentin-mac%C3%A9-310683165/) – [YouTube](https://www.youtube.com/channel/UCMIW0JKxoxBDM5yiiF17SrA) – valentin.mace@kedgebs.com

Distributed under the MIT license. See ``LICENSE`` for more information.
