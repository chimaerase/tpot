"""
This file is part of the TPOT library.

The current version of TPOT was developed at Cedars-Sinai by:
    - Pedro Henrique Ribeiro (https://github.com/perib, https://www.linkedin.com/in/pedro-ribeiro/)
    - Anil Saini (anil.saini@cshs.org)
    - Jose Hernandez (jgh9094@gmail.com)
    - Jay Moran (jay.moran@cshs.org)
    - Nicholas Matsumoto (nicholas.matsumoto@cshs.org)
    - Hyunjun Choi (hyunjun.choi@cshs.org)
    - Gabriel Ketron (gabriel.ketron@cshs.org)
    - Miguel E. Hernandez (miguel.e.hernandez@cshs.org)
    - Jason Moore (moorejh28@gmail.com)

The original version of TPOT was primarily developed at the University of Pennsylvania by:
    - Randal S. Olson (rso@randalolson.com)
    - Weixuan Fu (weixuanf@upenn.edu)
    - Daniel Angell (dpa34@drexel.edu)
    - Jason Moore (moorejh28@gmail.com)
    - and many more generous open-source contributors

TPOT is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

TPOT is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with TPOT. If not, see <http://www.gnu.org/licenses/>.

"""
from sklearn.base import TransformerMixin, BaseEstimator 
import numpy as np

class Passthrough(TransformerMixin,BaseEstimator):
    """
    A transformer that does nothing. It just passes the input array as is.
    """

    def fit(self, X=None, y=None):
        """
        Nothing to fit, just returns self.
        """
        return self

    def transform(self, X):
        """
        returns the input array as is.
        """
        return X


class SkipTransformer(TransformerMixin,BaseEstimator):
    """
    A transformer returns an empty array. When combined with FeatureUnion, it can be used to skip a branch.
    """
    def fit(self, X=None, y=None):
        """
        Nothing to fit, just returns self.
        """
        return self

    def transform(self, X):
        """
        returns an empty array.
        """
        return np.array([]).reshape(X.shape[0],0)
    
