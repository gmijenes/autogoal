# AUTOGENERATED ON 2020-02-01 12:18:14.877438
## DO NOT MODIFY THIS FILE MANUALLY

from autogoal.grammar import (
    ContinuousValue,
    DiscreteValue,
    CategoricalValue,
    BooleanValue,
)
from autogoal.contrib.nltk._builder import (
    NltkStemmer,
    NltkTokenizer,
    NltkLemmatizer,
    NltkTagger,
    NltkTrainedTagger,
)
from autogoal.kb import Word, Stem, Sentence, Seq, Postag, Document, algorithm
from autogoal.kb import Supervised
from autogoal.utils import nice_repr
from numpy import inf, nan

from nltk.stem.cistem import Cistem as _Cistem


@nice_repr
class Cistem(_Cistem, NltkStemmer):
    def __init__(self, case_insensitive: BooleanValue()):
        self.case_insensitive = case_insensitive
        NltkStemmer.__init__(self)
        _Cistem.__init__(self, case_insensitive=case_insensitive)

    def run(self, input: Word) -> Stem:
        return NltkStemmer.run(self, input)


from nltk.stem.isri import ISRIStemmer as _ISRIStemmer


@nice_repr
class ISRIStemmer(_ISRIStemmer, NltkStemmer):
    def __init__(self,):

        NltkStemmer.__init__(self)
        _ISRIStemmer.__init__(self,)

    def run(self, input: Word) -> Stem:
        return NltkStemmer.run(self, input)


from nltk.stem.lancaster import LancasterStemmer as _LancasterStemmer


@nice_repr
class LancasterStemmer(_LancasterStemmer, NltkStemmer):
    def __init__(self, strip_prefix_flag: BooleanValue()):
        self.strip_prefix_flag = strip_prefix_flag
        NltkStemmer.__init__(self)
        _LancasterStemmer.__init__(self, strip_prefix_flag=strip_prefix_flag)

    def run(self, input: Word) -> Stem:
        return NltkStemmer.run(self, input)


from nltk.stem.porter import PorterStemmer as _PorterStemmer


@nice_repr
class PorterStemmer(_PorterStemmer, NltkStemmer):
    def __init__(self,):

        NltkStemmer.__init__(self)
        _PorterStemmer.__init__(self,)

    def run(self, input: Word) -> Stem:
        return NltkStemmer.run(self, input)


from nltk.stem.rslp import RSLPStemmer as _RSLPStemmer


@nice_repr
class RSLPStemmer(_RSLPStemmer, NltkStemmer):
    def __init__(self,):

        NltkStemmer.__init__(self)
        _RSLPStemmer.__init__(self,)

    def run(self, input: Word) -> Stem:
        return NltkStemmer.run(self, input)


from nltk.stem.snowball import SnowballStemmer as _SnowballStemmer


@nice_repr
class SnowballStemmer(_SnowballStemmer, NltkStemmer):
    def __init__(
        self,
        language: CategoricalValue(
            "italian",
            "portuguese",
            "hungarian",
            "english",
            "german",
            "arabic",
            "danish",
            "norwegian",
            "finnish",
            "dutch",
            "romanian",
            "russian",
            "swedish",
            "spanish",
            "french",
        ),
    ):
        self.language = language
        NltkStemmer.__init__(self)
        _SnowballStemmer.__init__(self, language=language)

    def run(self, input: Word) -> Stem:
        return NltkStemmer.run(self, input)


from nltk.stem.wordnet import WordNetLemmatizer as _WordNetLemmatizer


@nice_repr
class WordNetLemmatizer(_WordNetLemmatizer, NltkLemmatizer):
    def __init__(self,):

        NltkLemmatizer.__init__(self)
        _WordNetLemmatizer.__init__(self,)

    def run(self, input: Word) -> Stem:
        return NltkLemmatizer.run(self, input)


from nltk.tag.perceptron import PerceptronTagger as _PerceptronTagger


@nice_repr
class PerceptronTagger(_PerceptronTagger, NltkTrainedTagger):
    def __init__(self,):

        NltkTrainedTagger.__init__(self)
        _PerceptronTagger.__init__(self,)

    def run(self, input: Seq[Word]) -> Seq[Postag]:
        return NltkTrainedTagger.run(self, input)


from nltk.tag.sequential import AffixTagger as _AffixTagger


@nice_repr
class AffixTagger(NltkTagger):
    def __init__(
        self,
        affix_length: DiscreteValue(min=2, max=6),
        min_stem_length: DiscreteValue(min=1, max=4),
        cutoff: DiscreteValue(min=0, max=10),
        backoff: algorithm(
            Seq[Seq[Word]], Supervised[Seq[Seq[Postag]]], Seq[Seq[Postag]]
        ),
    ):
        self.affix_length = affix_length
        self.min_stem_length = min_stem_length
        self.cutoff = cutoff
        self.backoff = backoff
        self.tagger = _AffixTagger

        self.values = dict(
            affix_length=affix_length,
            min_stem_length=min_stem_length,
            cutoff=cutoff,
            backoff=backoff,
        )

        NltkTagger.__init__(self)

    def run(
        self, input: Seq[Seq[Word]], y: Supervised[Seq[Seq[Postag]]]
    ) -> Seq[Seq[Postag]]:
        return NltkTagger.run(self, input, y)


from nltk.tag.sequential import BigramTagger as _BigramTagger


@nice_repr
class BigramTagger(NltkTagger):
    def __init__(
        self, cutoff: DiscreteValue(min=0, max=10),
    ):
        self.cutoff = cutoff
        self.tagger = _BigramTagger
        self.values = dict(cutoff=cutoff)

        NltkTagger.__init__(self)

    def run(
        self, input: Seq[Seq[Word]], y: Supervised[Seq[Seq[Postag]]]
    ) -> Seq[Seq[Postag]]:
        return NltkTagger.run(self, input, y)


from nltk.tag.sequential import ClassifierBasedPOSTagger as _ClassifierBasedPOSTagger


@nice_repr
class ClassifierBasedPOSTagger(NltkTagger):
    def __init__(self,):

        self.tagger = _ClassifierBasedPOSTagger
        self.values = dict()

        NltkTagger.__init__(self)

    def run(
        self, input: Seq[Seq[Word]], y: Supervised[Seq[Seq[Postag]]]
    ) -> Seq[Seq[Postag]]:
        return NltkTagger.run(self, input, y)


from nltk.tag.sequential import TrigramTagger as _TrigramTagger


@nice_repr
class TrigramTagger(NltkTagger):
    def __init__(
        self, cutoff: DiscreteValue(min=0, max=10),
    ):
        self.cutoff = cutoff
        self.tagger = _TrigramTagger
        self.values = dict(cutoff=cutoff)

        NltkTagger.__init__(self)

    def run(
        self, input: Seq[Seq[Word]], y: Supervised[Seq[Seq[Postag]]]
    ) -> Seq[Seq[Postag]]:
        return NltkTagger.run(self, input, y)


from nltk.tag.sequential import UnigramTagger as _UnigramTagger


@nice_repr
class UnigramTagger(NltkTagger):
    def __init__(
        self, cutoff: DiscreteValue(min=0, max=10),
    ):
        self.cutoff = cutoff
        self.tagger = _UnigramTagger
        self.values = dict(cutoff=cutoff)

        NltkTagger.__init__(self)

    def run(
        self, input: Seq[Seq[Word]], y: Supervised[Seq[Seq[Postag]]]
    ) -> Seq[Seq[Postag]]:
        return NltkTagger.run(self, input, y)


from nltk.tag.tnt import TnT as _TnT


@nice_repr
class TnT(_TnT, NltkTrainedTagger):
    def __init__(
        self,
        Trained: BooleanValue(),
        N: DiscreteValue(min=500, max=2000),
        C: BooleanValue(),
    ):
        self.Trained = Trained
        self.N = N
        self.C = C
        NltkTrainedTagger.__init__(self)
        _TnT.__init__(self, Trained=Trained, N=N, C=C)

    def run(self, input: Seq[Word]) -> Seq[Postag]:
        return NltkTrainedTagger.run(self, input)


from nltk.tokenize.casual import TweetTokenizer as _TweetTokenizer


@nice_repr
class TweetTokenizer(_TweetTokenizer, NltkTokenizer):
    def __init__(
        self,
        preserve_case: BooleanValue(),
        reduce_len: BooleanValue(),
        strip_handles: BooleanValue(),
    ):
        self.preserve_case = preserve_case
        self.reduce_len = reduce_len
        self.strip_handles = strip_handles
        NltkTokenizer.__init__(self)
        _TweetTokenizer.__init__(
            self,
            preserve_case=preserve_case,
            reduce_len=reduce_len,
            strip_handles=strip_handles,
        )

    def run(self, input: Sentence) -> Seq[Word]:
        return NltkTokenizer.run(self, input)


from nltk.tokenize.mwe import MWETokenizer as _MWETokenizer


@nice_repr
class MWETokenizer(_MWETokenizer, NltkTokenizer):
    def __init__(self,):

        NltkTokenizer.__init__(self)
        _MWETokenizer.__init__(self,)

    def run(self, input: Sentence) -> Seq[Word]:
        return NltkTokenizer.run(self, input)


from nltk.tokenize.punkt import PunktSentenceTokenizer as _PunktSentenceTokenizer


@nice_repr
class PunktSentenceTokenizer(_PunktSentenceTokenizer, NltkTokenizer):
    def __init__(self,):

        NltkTokenizer.__init__(self)
        _PunktSentenceTokenizer.__init__(self,)

    def run(self, input: Document) -> Seq[Sentence]:
        return NltkTokenizer.run(self, input)


from nltk.tokenize.regexp import BlanklineTokenizer as _BlanklineTokenizer


@nice_repr
class BlanklineTokenizer(_BlanklineTokenizer, NltkTokenizer):
    def __init__(self,):

        NltkTokenizer.__init__(self)
        _BlanklineTokenizer.__init__(self,)

    def run(self, input: Document) -> Seq[Sentence]:
        return NltkTokenizer.run(self, input)


from nltk.tokenize.regexp import WhitespaceTokenizer as _WhitespaceTokenizer


@nice_repr
class WhitespaceTokenizer(_WhitespaceTokenizer, NltkTokenizer):
    def __init__(self,):

        NltkTokenizer.__init__(self)
        _WhitespaceTokenizer.__init__(self,)

    def run(self, input: Sentence) -> Seq[Word]:
        return NltkTokenizer.run(self, input)


from nltk.tokenize.regexp import WordPunctTokenizer as _WordPunctTokenizer


@nice_repr
class WordPunctTokenizer(_WordPunctTokenizer, NltkTokenizer):
    def __init__(self,):

        NltkTokenizer.__init__(self)
        _WordPunctTokenizer.__init__(self,)

    def run(self, input: Sentence) -> Seq[Word]:
        return NltkTokenizer.run(self, input)


from nltk.tokenize.sexpr import SExprTokenizer as _SExprTokenizer


@nice_repr
class SExprTokenizer(_SExprTokenizer, NltkTokenizer):
    def __init__(self, strict: BooleanValue()):
        self.strict = strict
        NltkTokenizer.__init__(self)
        _SExprTokenizer.__init__(self, strict=strict)

    def run(self, input: Document) -> Seq[Sentence]:
        return NltkTokenizer.run(self, input)


from nltk.tokenize.simple import LineTokenizer as _LineTokenizer


@nice_repr
class LineTokenizer(_LineTokenizer, NltkTokenizer):
    def __init__(self,):

        NltkTokenizer.__init__(self)
        _LineTokenizer.__init__(self,)

    def run(self, input: Document) -> Seq[Sentence]:
        return NltkTokenizer.run(self, input)


from nltk.tokenize.simple import SpaceTokenizer as _SpaceTokenizer


@nice_repr
class SpaceTokenizer(_SpaceTokenizer, NltkTokenizer):
    def __init__(self,):

        NltkTokenizer.__init__(self)
        _SpaceTokenizer.__init__(self,)

    def run(self, input: Sentence) -> Seq[Word]:
        return NltkTokenizer.run(self, input)


from nltk.tokenize.simple import TabTokenizer as _TabTokenizer


@nice_repr
class TabTokenizer(_TabTokenizer, NltkTokenizer):
    def __init__(self,):

        NltkTokenizer.__init__(self)
        _TabTokenizer.__init__(self,)

    def run(self, input: Document) -> Seq[Sentence]:
        return NltkTokenizer.run(self, input)


from nltk.tokenize.toktok import ToktokTokenizer as _ToktokTokenizer


@nice_repr
class ToktokTokenizer(_ToktokTokenizer, NltkTokenizer):
    def __init__(self,):

        NltkTokenizer.__init__(self)
        _ToktokTokenizer.__init__(self,)

    def run(self, input: Sentence) -> Seq[Word]:
        return NltkTokenizer.run(self, input)


from nltk.tokenize.treebank import TreebankWordTokenizer as _TreebankWordTokenizer


@nice_repr
class TreebankWordTokenizer(_TreebankWordTokenizer, NltkTokenizer):
    def __init__(self,):

        NltkTokenizer.__init__(self)
        _TreebankWordTokenizer.__init__(self,)

    def run(self, input: Sentence) -> Seq[Word]:
        return NltkTokenizer.run(self, input)


from nltk.tag.perceptron import PerceptronTagger as _PerceptronTagger


@nice_repr
class PerceptronTagger(_PerceptronTagger, NltkTrainedTagger):
    def __init__(self,):

        NltkTrainedTagger.__init__(self)
        _PerceptronTagger.__init__(self,)

    def run(self, input: Seq[Word]) -> Seq[Postag]:
        return NltkTrainedTagger.run(self, input)


from nltk.tag.sequential import BigramTagger as _BigramTagger


@nice_repr
class BigramTagger(NltkTagger):
    def __init__(
        self, cutoff: DiscreteValue(min=0, max=10),
    ):
        self.cutoff = cutoff
        self.tagger = _BigramTagger
        self.values = dict(cutoff=cutoff)

        NltkTagger.__init__(self)

    def run(
        self, input: Seq[Seq[Word]], y: Supervised[Seq[Seq[Postag]]]
    ) -> Seq[Seq[Postag]]:
        return NltkTagger.run(self, input, y)


from nltk.tag.sequential import ClassifierBasedPOSTagger as _ClassifierBasedPOSTagger


@nice_repr
class ClassifierBasedPOSTagger(NltkTagger):
    def __init__(self,):

        self.tagger = _ClassifierBasedPOSTagger
        self.values = dict()

        NltkTagger.__init__(self)

    def run(
        self, input: Seq[Seq[Word]], y: Supervised[Seq[Seq[Postag]]]
    ) -> Seq[Seq[Postag]]:
        return NltkTagger.run(self, input, y)


from nltk.tag.sequential import TrigramTagger as _TrigramTagger


@nice_repr
class TrigramTagger(NltkTagger):
    def __init__(
        self, cutoff: DiscreteValue(min=0, max=10),
    ):
        self.cutoff = cutoff
        self.tagger = _TrigramTagger
        self.values = dict(cutoff=cutoff)

        NltkTagger.__init__(self)

    def run(
        self, input: Seq[Seq[Word]], y: Supervised[Seq[Seq[Postag]]]
    ) -> Seq[Seq[Postag]]:
        return NltkTagger.run(self, input, y)


from nltk.tag.sequential import UnigramTagger as _UnigramTagger


@nice_repr
class UnigramTagger(NltkTagger):
    def __init__(
        self, cutoff: DiscreteValue(min=0, max=10),
    ):
        self.cutoff = cutoff
        self.tagger = _UnigramTagger
        self.values = dict(cutoff=cutoff)

        NltkTagger.__init__(self)

    def run(
        self, input: Seq[Seq[Word]], y: Supervised[Seq[Seq[Postag]]]
    ) -> Seq[Seq[Postag]]:
        return NltkTagger.run(self, input, y)


from nltk.tag.tnt import TnT as _TnT


@nice_repr
class TnT(_TnT, NltkTrainedTagger):
    def __init__(
        self,
        Trained: BooleanValue(),
        N: DiscreteValue(min=500, max=2000),
        C: BooleanValue(),
    ):
        self.Trained = Trained
        self.N = N
        self.C = C
        NltkTrainedTagger.__init__(self)
        _TnT.__init__(self, Trained=Trained, N=N, C=C)

    def run(self, input: Seq[Word]) -> Seq[Postag]:
        return NltkTrainedTagger.run(self, input)


__all__ = [
    "Cistem",
    "ISRIStemmer",
    "LancasterStemmer",
    "PorterStemmer",
    "RSLPStemmer",
    "SnowballStemmer",
    "WordNetLemmatizer",
    "PerceptronTagger",
    "AffixTagger",
    "BigramTagger",
    "ClassifierBasedPOSTagger",
    "TrigramTagger",
    "UnigramTagger",
    "TweetTokenizer",
    "MWETokenizer",
    "PunktSentenceTokenizer",
    "BlanklineTokenizer",
    "WhitespaceTokenizer",
    "WordPunctTokenizer",
    "SExprTokenizer",
    "LineTokenizer",
    "SpaceTokenizer",
    "TabTokenizer",
    "ToktokTokenizer",
    "TreebankWordTokenizer",
    "PerceptronTagger",
    "BigramTagger",
    "ClassifierBasedPOSTagger",
    "TrigramTagger",
    "UnigramTagger",
    "TnT",
]
