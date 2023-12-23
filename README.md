The various techniques presented in this chapter (recursion, memoization, compres-
sion, and manipulation at the bit level) are so common in modern software develop-
ment that it is impossible to imagine the world of computing without them. Although
problems can be solved without them, it is often more logical or performant to solve
problems with them.
Recursion, in particular, is at the heart of not just many algorithms, but even whole
programming languages. In some functional programming languages, like Scheme
and Haskell, recursion takes the place of the loops used in imperative languages. It is
worth remembering, though, that anything accomplishable with a recursive technique
is also accomplishable with an iterative technique.
Memoization has been applied successfully to speed up the work of parsers (pro-
grams that interpret languages). It is useful in all problems where the result of a
recent calculation will likely be asked for again. Another application of memoization
is in language runtimes. Some language runtimes (versions of Prolog, for instance)
will store the results of function calls automatically (auto-memoization), so that the func-
tion need not execute the next time the same call is made. This is similar to how the
@lru_cache() decorator in fib6() worked.
Compression has made an internet-connected world constrained by bandwidth
more tolerable. The bit-string technique examined in section 1.2 is usable for real-
world simple data types that have a limited number of possible values, for which even
a byte is overkill. The majority of compression algorithms, however, operate by finding
patterns or structures within a data set that allow for repeated information to be elim-
inated. They are significantly more complicated than what is covered in section 1.2.
One-time pads are not practical for general encryption. They require both the
encrypter and the decrypter to have possession of one of the keys (the dummy data in
our example) for the original data to be reconstructed, which is cumbersome and
defeats the goal of most encryption schemes (keeping keys secret). But you may be inter-
ested to know that the name “one-time pad” comes from spies using real paper pads with
dummy data on them to create encrypted communications during the Cold War.
These techniques are programmatic building blocks that other algorithms are
built on top of.
