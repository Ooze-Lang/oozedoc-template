"""Pygments lexer for Ooze source and declaration snippets."""

from pygments.lexer import RegexLexer, bygroups, words
from pygments.token import Comment, Keyword, Name, Number, Operator, Punctuation, String, Whitespace


class OozeLexer(RegexLexer):
    name = "Ooze"
    aliases = ["ooze"]
    filenames = ["*.oz"]
    mimetypes = ["text/x-ooze"]

    tokens = {
        "root": [
            (r"\s+", Whitespace),
            (r"//[^\n]*", Comment.Single),
            (r"/\*", Comment.Multiline, "comment"),
            (r'([A-Za-z_]\w*)(")', bygroups(String.Affix, String.Double), "string"),
            (r'"', String.Double, "string"),
            (r"'(?:\\.|[^'\\])*'", String.Char),
            (r"0x[0-9a-fA-F_]+", Number.Hex),
            (r"0b[01_]+", Number.Bin),
            (r"0o[0-7_]+", Number.Oct),
            (r"0d[0-9_]+", Number.Integer),
            (r"[0-9][0-9_]*(?:\.[0-9][0-9_]*)[eE][+-]?[0-9][0-9_]*", Number.Float),
            (r"[0-9][0-9_]*[eE][+-]?[0-9][0-9_]*", Number.Float),
            (r"[0-9][0-9_]*\.[0-9][0-9_]*", Number.Float),
            (r"[0-9][0-9_]*", Number.Integer),
            (words(("true", "false", "null"), suffix=r"\b"), Keyword.Constant),
            (words(("is", "isnt", "as"), suffix=r"\b"), Operator.Word),
            (r"(fn|macro)(\s+)([A-Za-z_]\w*)", bygroups(Keyword.Declaration, Whitespace, Name.Function)),
            (r"(type|trait)(\s+)([A-Za-z_]\w*)", bygroups(Keyword.Declaration, Whitespace, Name.Class)),
            (words(("struct", "enum", "fn", "macro", "type", "trait", "impl", "import"),
                   suffix=r"\b"), Keyword.Declaration),
            (words(("implicit", "explicit", "static", "thread_local", "pub", "mut", "auto"),
                   suffix=r"\b"), Keyword),
            (words(("quote", "while", "if", "else", "switch", "continue", "break", "defer",
                    "synchronized", "return", "yield", "async", "sizeof", "alignof", "typeof",
                    "await", "let", "for", "forall", "in", "out", "hold", "forbid", "forbids", "taints"),
                   suffix=r"\b"), Keyword),
            (words(("i8", "i16", "i32", "i64", "u8", "u16", "u32", "u64", "isize", "usize",
                    "f32", "f64", "bool", "void", "never", "Self"), suffix=r"\b"), Keyword.Type),
            (r"\$[A-Za-z_]\w*", Name.Variable),
            (r"[A-Za-z_]\w*(?=\s*\()", Name.Function),
            (r"[A-Z][A-Za-z_0-9]*", Name.Class),
            (r"[A-Za-z_]\w*", Name),
            (r"<=>|<<=|>>=|\?\?=|\.\.\.|->|=>|::|<<|>>|&&|\|\||\?\?|\?\.|\.\.|[+*/%=&|^!<>-]=?", Operator),
            (r"[~?@$]", Operator),
            (r"[{}()\[\],:;.#]", Punctuation),
        ],
        "comment": [
            (r"/\*", Comment.Multiline, "#push"),
            (r"\*/", Comment.Multiline, "#pop"),
            (r"[^*/]+|[*/]", Comment.Multiline),
        ],
        "string": [
            (r'"', String.Double, "#pop"),
            (r"\\.", String.Escape),
            (r'[^"\\]+', String.Double),
        ],
    }
