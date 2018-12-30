Introduction
============

``Zezima Ciphers`` will be a simple API that will encode and decode messages using several popular ciphers.

The aim of the project is to produce an API that uses  FLASK etc ,Cryptology course work and Sphinx documentation.The entire project is done in Python 3 and Tested on Linux Mint.

Motivation
**********

The project will hopefully provided inspiration and reference material for future students of Cryptology.It is to combine two seperate projects and to furtheur understand the Flask framework.
Did you ever hear the tragedy of Darth Plagueis the Wise?

I thought not. It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life.He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful.. the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. It's ironic he could save others from death, but not himself.

Limitations
***********

- The Ciphers can not brute force decode the messages so the private keys or the shared inforamtion must be supplied to the api in order to function.
- Jefferson Wheel Cipher is currently always fixed so the private key is the wheel offset.
- Enigma is restricted to M3 device, and doesn;t account for Kriegsmarine.

