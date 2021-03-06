"""Contains tests for the model abstractions and different models."""
import unittest
import os
import shutil

from hbaselines.utils.train import parse_options
from experiments.run_fcnet import main as run_fcnet
from experiments.run_hrl import main as run_hrl


class TestExperimentRunnerScripts(unittest.TestCase):
    """Tests the runner scripts in the experiments folder."""

    def test_run_fcent_td3(self):
        # Run the script; verify it executes without failure.
        args = parse_options('', '', args=["MountainCarContinuous-v0",
                                           "--n_cpus", "1",
                                           "--total_steps", "2000"])
        run_fcnet(args, 'data/fcnet')

        # Check that the folders were generated.
        self.assertTrue(os.path.isdir(
            os.path.join(os.getcwd(), "data/fcnet/MountainCarContinuous-v0")))

        # Clear anything that was generated.
        shutil.rmtree(os.path.join(os.getcwd(), "data"))

    def test_run_fcent_sac(self):
        # Run the script; verify it executes without failure.
        args = parse_options('', '', args=["MountainCarContinuous-v0",
                                           "--n_cpus", "1",
                                           "--total_steps", "2000",
                                           "--alg", "SAC"])
        run_fcnet(args, 'data/fcnet')

        # Check that the folders were generated.
        self.assertTrue(os.path.isdir(
            os.path.join(os.getcwd(), "data/fcnet/MountainCarContinuous-v0")))

        # Clear anything that was generated.
        shutil.rmtree(os.path.join(os.getcwd(), "data"))

    def test_run_fcent_failure(self):
        # Run the script; verify it fails.
        args = parse_options('', '', args=["MountainCarContinuous-v0",
                                           "--n_cpus", "1",
                                           "--total_steps", "2000",
                                           "--alg", "woops"])

        self.assertRaises(ValueError, run_fcnet,
                          args=args, base_dir='data/fcnet')

        # Clear anything that was generated.
        shutil.rmtree(os.path.join(os.getcwd(), "data"))

    def test_run_hrl_td3(self):
        # Run the script; verify it executes without failure.
        args = parse_options('', '', args=["MountainCarContinuous-v0",
                                           "--n_cpus", "1",
                                           "--total_steps", "2000"])
        run_hrl(args, 'data/goal-conditioned')

        # Check that the folders were generated.
        self.assertTrue(os.path.isdir(
            os.path.join(
                os.getcwd(),
                "data/goal-conditioned/MountainCarContinuous-v0")))

        # Clear anything that was generated.
        shutil.rmtree(os.path.join(os.getcwd(), "data"))

    def test_run_hrl_sac(self):
        # Run the script; verify it executes without failure.
        args = parse_options('', '', args=["MountainCarContinuous-v0",
                                           "--n_cpus", "1",
                                           "--total_steps", "2000",
                                           "--alg", "SAC"])
        run_hrl(args, 'data/goal-conditioned')

        # Check that the folders were generated.
        self.assertTrue(os.path.isdir(
            os.path.join(
                os.getcwd(),
                "data/goal-conditioned/MountainCarContinuous-v0")))

        # Clear anything that was generated.
        shutil.rmtree(os.path.join(os.getcwd(), "data"))

    def test_run_hrl_failure(self):
        # Run the script; verify it executes without failure.
        args = parse_options('', '', args=["MountainCarContinuous-v0",
                                           "--n_cpus", "1",
                                           "--total_steps", "2000",
                                           "--alg", "woops"])

        self.assertRaises(ValueError, run_hrl,
                          args=args, base_dir='data/goal-conditioned')

        # Clear anything that was generated.
        shutil.rmtree(os.path.join(os.getcwd(), "data"))


if __name__ == '__main__':
    unittest.main()
