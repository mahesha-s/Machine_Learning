################################################################################
#                                                                              #
#                                  Learner:                                    #
#                                                                              #
################################################################################
#                                                                              #
# This module defines a class Learner which handles different learners         #
#                                                                              #
################################################################################



#------------------------------------------------------------------------------#
# import built-in system modules here                                          #
#------------------------------------------------------------------------------#
import os
import sys
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# import package modules here                                                  #
#------------------------------------------------------------------------------#
import sources.utility.util as util
import sources.learner.linear_regression as lin
import sources.learner.logistic_regression as log
import sources.learner.k_mean_clustering as kmc
import sources.learner.hierarchical_clustering as hrc
import sources.learner.classification_tree as cla
import sources.learner.random_forest as rf
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# Learner Class                                                                #
#------------------------------------------------------------------------------#
class Learner:
      # data members
      training_data = None
      test_data = None
      kind = None

      # special init method
      def __init__(self, training_data, test_data, kind):
          self.training_data = training_data
          self.test_data = test_data
          self.kind = kind

      # random forest 
      def __random_forest(self):
         rfo = rf.RandomForest()
         roots = rfo.learn(self.training_data)
         class_dict = rfo.classify(roots, self.test_data)
         correct_class_dict = util.get_correct_class_dict_for_random_forest()
         util.print_random_forest_output(self.test_data, roots, class_dict,
                                         correct_class_dict)

      # classification tree
      def __classification_tree(self):
         clo = cla.ClassificationTree()
         root = clo.learn(self.training_data)
         class_dict = clo.classify(root, self.test_data)
         correct_class_dict = \
                           util.get_correct_class_dict_for_classification_tree()
         util.print_classification_tree_output(self.test_data, root, class_dict,
                                               correct_class_dict)

      # hierarchical clustering
      def __hierarchical_clustering(self):
         hro = hrc.HierarchicalCluster()
         cluster_list = hro.cluster(self.training_data)
         util.print_hierarchical_clustering_output(cluster_list)

      # k-mean clustering
      def __k_mean_clustering(self):
         kmo = kmc.KMeanCluster()
         i_mat, cluster, final_centroids = kmo.cluster(self.training_data)
         sse = util.compute_sum_squared_error(i_mat, cluster, final_centroids)
         util.print_k_mean_clustering_output(cluster, sse)

      # logistic regression learner
      def __logistic_regression(self):
          lro = log.LogisticRegression()
          r_vec = lro.learn(self.training_data)
          o_vec, p_vec = lro.predict(self.test_data, r_vec)
          error, accuracy = util.compute_error_and_accuracy(o_vec, p_vec)
          util.print_logistic_regression_output(o_vec, p_vec, error, accuracy)

      # linear regression learner
      def __linear_regression(self):
          gro = lin.LinearRegression()
          r_vec = gro.learn(self.training_data)
          o_vec, p_vec = gro.predict(self.test_data, r_vec)
          mse = util.compute_mean_squared_error(o_vec, p_vec)
          util.print_linear_regression_output(o_vec, p_vec, mse)

      # public interface function of the class Learner
      def learn_and_predict(self):
          os.system("clear")
          print("\n\nBe patient... I am learning...")

          # call learner based on user choice
          if self.kind == 1:
             self.__linear_regression()
          elif self.kind == 2:
             self.__logistic_regression()
          elif self.kind == 3:
             self.__k_mean_clustering()
          elif self.kind == 4:
             self.__hierarchical_clustering()
          elif self.kind == 5:
             self.__classification_tree()
          elif self.kind == 6:
             self.__random_forest()
#------------------------------------------------------------------------------#
