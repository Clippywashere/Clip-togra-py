# Clip-togra-py?

Clip-togra-py is a CLI-based cryptography multitool used to encrypt and decrypt various classical ciphers (also includes a few useful tools)

## Description

Clip-togra-py can handle the encryption and decryption of various classical ciphers when the method and relevant information is known (it is in essence multiple encrypters and decrypters combined into one multitool!) it also has many cipher-specific features (Ex: regularity in columnar transposition) and general features such as dual execution modes.

WARNING: Classical Ciphers are NOT adequate for real-life security applications and must NOT be used to protect any important information.

## Dependencies and Requirements

Python inbuilt modules math and random
Python 3.10+ (Match cases)

## Contributions

NO contributions accepted as Clip-togra-py is a solo project to learn more about both Cryptography and Programming
Suggestions and Bug reports are welcome!

## Execution modes:

Interactive:
Allows single-process execution multiple sequencial inputs

Chaining:
Allows multiple similar process execution with a single input

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
4. Adding support for more classical ciphers (ADFGX, Rail fence, Double Transposition etc.)