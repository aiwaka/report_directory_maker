latex_template = r"""\RequirePackage{{plautopatch}}
\documentclass[uplatex,a4paper,dvipdfmx]{{jsarticle}}
\input{{./preamble.tex}}

\title{{{title}}}
\author{{{author}}}
\date{{\today}}

\begin{{document}}
\maketitle



\begin{{thebibliography}}{{9}}
  \bibitem{{a}} reference a
\end{{thebibliography}}

\end{{document}}
"""
