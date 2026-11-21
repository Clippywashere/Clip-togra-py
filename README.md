# Clip-togra-py?

Clip-togra-py is a CLI-based cryptography multitool used to encrypt and decrypt various classical ciphers (also includes a few useful tools)

## Description

Clip-togra-py can handle the encryption and decryption of various classical ciphers when the method and relevant information are known (it is in essence multiple encrypters and decrypters combined into one multitool!) 

It also has many cipher-specific features (Ex: regularity in columnar transposition) and general features such as dual execution modes.

This project aims to provide a simple, extensible and modular environment for experimenting and learning about Classical Cryptography while exploring their implementation through Python

WARNING: Classical Ciphers are NOT adequate for real-life security applications and must NOT be used to protect any important information.

## Dependencies and Requirements

Python inbuilt modules math and random
Python 3.10+ (Match cases)

## Contributions

NO contributions accepted
Suggestions and Bug reports are welcome!

## Execution modes:

Interactive:

Allows individual processes to be performed via interactive sequential user inputs

Chaining:

Allows multiple similar (encryption only or decryption only) processes to be combined and executed sequentially through a single input

Chaining is designed to provide streamlined execution of multiplr processes (essentially the ability to execute complex cryptosystems)

## Supported ciphers:

Bifid, Affine, Book, Morse, Nihilist, Playfair, Tapcode, Columnar Transposition*

Pseudomorse (self-created obfuscation cipher)

*Encryption only (Decryption feature will be rolled out soon)

## Available tools:

Frequency analyzer and Frequency matcher (Heuristic)

## LICENSE:

MIT License
Refer to LICENSE.md

### Roadmap (TODO)

1. Bug hunting and minor improvements
2. Adding chain validation
3. Decryption function for Columnar Transposition
5. Adding support for more cryptanalysis tools
4. Adding support for more classical ciphers (ADFGX, Rail fence, Double Transposition etc.)