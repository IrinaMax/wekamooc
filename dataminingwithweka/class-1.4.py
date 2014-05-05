# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Data Mining with Weka - Class 1.4
# Copyright (C) 2014 Fracpete (fracpete at gmail dot com)

import os
import weka.core.jvm as jvm
from weka.core.converters import Loader
from weka.core.classes import Random
from weka.classifiers import Classifier, Evaluation
import weka.plot.graph as plg

jvm.start()

# TODO
# wherever your datasets are located
data_dir = "/some/where/data"

# load glass
fname = data_dir + os.sep + "glass.arff"
print("\nLoading dataset: " + fname + "\n")
loader = Loader(classname="weka.core.converters.ArffLoader")
data = loader.load_file(fname)
data.set_class_index(data.num_attributes() - 1)

# cross-validate default J48
print("\nDefault J48")
cls = Classifier(classname="weka.classifiers.trees.J48")
evl = Evaluation(data)
evl.crossvalidate_model(cls, data, 10, Random(1))
print(evl.to_summary())
print(evl.to_matrix())

# build and plot model
cls.build_classifier(data)
plg.plot_dot_graph(cls.graph())

# cross-validate unpruned J48 with larger leaf size
print("\nUnpruned J48 (minNumObj=15)")
cls = Classifier(classname="weka.classifiers.trees.J48", options=["-U", "-M", "15"])
evl = Evaluation(data)
evl.crossvalidate_model(cls, data, 10, Random(1))
print(evl.to_summary())
print(evl.to_matrix())

# build and plot model
cls.build_classifier(data)
plg.plot_dot_graph(cls.graph())

jvm.stop()
