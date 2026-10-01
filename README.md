# Clip-togra-py?

Clip-togra-py is a cryptography multitool used to encrypt and decrypt various classical ciphers (also includes a few useful tools)

## Description

Clip-togra-py can handle the encryption and decryption of various classical ciphers when the method and relevant keys are known (it is in essence multiple encrypters and decrypters combined into one multitool!) 

WARNING: Classical Ciphers are NOT adequate for real-life security applications and must NOT be used to protectany important information

## Dependencies

Python inbuilt modules math and random

## Contributions

NO contributions are accepted as this is a solo project to learn more about both Cryptography and Programming

## Supported ciphers:

Bifid, Affine, Book, Morse, Nihilist, Playfair, Tapcode, Columnar Transposition*

Pseudomorse (self-created obfuscation cipher)

*Encryption only (Decryption feature will be rolled out soon)

## Available tools:

Frequency analyzer and Frequency matcher(Heuristic)

### Roadmap (TODO)

1. Decryption function for Columnar Transposition
2. Standardizing methods across files (including input validation)
3. Simplifying the choice based UI (not exactly much of a UI rn)
4. Adding support for more classical ciphers (ADFGX, Rail fence, Double Transposition etc.)
5. Adding support for chaining ciphers