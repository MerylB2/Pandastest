Sure, let's address each question step by step.

### Part 1: Understanding Limits

1. **Translation of \( \lim_{n \to \infty} U_n = l \)**

   This notation means that the limit of the sequence \( (U_n) \) as \( n \) approaches infinity equals \( l \). In other words, as \( n \) becomes very large, the terms \( U_n \) get arbitrarily close to \( l \).

### Part 2: Limit to Infinity

2. **Translation of \( \lim_{n \to \infty} U_n = +\infty \)**

   This means that for the sequence \( (U_n) \), as \( n \) goes to infinity, \( U_n \) becomes arbitrarily large. Formally, for every large number \( M \), there exists a number \( N \) such that for all \( n > N \), \( U_n > M \).

### Part 3: Limit of Rational Function \( f(x) = \frac{x^2 + 2x + 1}{x^2 - x - 1} \)

3. **Limits at \( \pm \infty \) and \( x \to \pm \infty \) for \( f(x) \):**

   Given \( f(x) = \frac{x^2 + 2x + 1}{x^2 - x - 1} \):

   - **Limit as \( x \to +\infty \)**:
     \[ \lim_{x \to +\infty} f(x) = \lim_{x \to +\infty} \frac{x^2 + 2x + 1}{x^2 - x - 1} = \frac{1}{1} = 1 \]

   - **Limit as \( x \to -\infty \)**:
     \[ \lim_{x \to -\infty} f(x) = \lim_{x \to -\infty} \frac{x^2 + 2x + 1}{x^2 - x - 1} = \frac{1}{1} = 1 \]

   Both limits at \( +\infty \) and \( -\infty \) are \( 1 \).

### Part 4: Limit of \( f(x) = \frac{\sqrt{x+1} - \sqrt{2x}}{x-1} \)

4. **Limits at \( \pm \infty \), \( x \to 1 \), for \( f(x) \):**

   Given \( f(x) = \frac{\sqrt{x+1} - \sqrt{2x}}{x-1} \):

   - **Limit as \( x \to +\infty \)**:
     \[ \lim_{x \to +\infty} f(x) = \lim_{x \to +\infty} \frac{\sqrt{x+1} - \sqrt{2x}}{x-1} = 0 \]

   - **Limit as \( x \to -\infty \)**:
     \[ \lim_{x \to -\infty} f(x) = \lim_{x \to -\infty} \frac{\sqrt{x+1} - \sqrt{2x}}{x-1} = 0 \]

   - **Limit as \( x \to 1 \)**:
     \[ \lim_{x \to 1} f(x) = \frac{\sqrt{1+1} - \sqrt{2 \cdot 1}}{1-1} = \frac{\sqrt{2} - \sqrt{2}}{0} \]

     This limit is indeterminate (\( \frac{0}{0} \)). We can apply L'Hôpital's rule:

     \[ \lim_{x \to 1} f(x) = \lim_{x \to 1} \frac{\frac{1}{2\sqrt{x+1}} - \frac{1}{\sqrt{2x}}}{1} \]

     \[ = \frac{\frac{1}{2\sqrt{2}} - \frac{1}{\sqrt{2}}}{1} = \frac{\frac{1 - 2}{2\sqrt{2}}}{1} = -\frac{1}{2\sqrt{2}} \]

     Simplifying further, \( \lim_{x \to 1} f(x) = -\frac{1}{2\sqrt{2}} \).

Therefore, the limits for \( f(x) \) are:
- \( \lim_{x \to +\infty} f(x) = 0 \)
- \( \lim_{x \to -\infty} f(x) = 0 \)
- \( \lim_{x \to 1} f(x) = -\frac{1}{2\sqrt{2}} \).