from __future__ import annotations

import unittest

from heeds.results_table import build_levels_table


class ResultsTableTests(unittest.TestCase):
    def test_same_response_name_from_two_studies_is_not_overwritten(self):
        studies = [
            {
                "id": "stress",
                "designs": [
                    {
                        "design_id": 1,
                        "inputs": {"thickness": 2.0},
                        "responses": {"mass": 10.0},
                    }
                ],
            },
            {
                "id": "crash",
                "designs": [
                    {
                        "design_id": 7,
                        "inputs": {"thickness": 2.0},
                        "responses": {"mass": 20.0},
                    }
                ],
            },
        ]

        table = build_levels_table(studies, [{"name": "thickness"}])

        self.assertEqual(
            table["columns"],
            ["水準", "thickness", "stress.mass", "crash.mass"],
        )
        self.assertEqual(table["rows"][0]["stress.mass"], 10.0)
        self.assertEqual(table["rows"][0]["crash.mass"], 20.0)

    def test_response_name_that_matches_input_is_namespaced(self):
        studies = [
            {
                "id": "stress",
                "designs": [
                    {
                        "design_id": 1,
                        "inputs": {"thickness": 2.0},
                        "responses": {"thickness": 99.0},
                    }
                ],
            }
        ]

        table = build_levels_table(studies, [{"name": "thickness"}])

        self.assertEqual(
            table["columns"],
            ["水準", "thickness", "stress.thickness"],
        )
        self.assertEqual(table["rows"][0]["thickness"], 2.0)
        self.assertEqual(table["rows"][0]["stress.thickness"], 99.0)


if __name__ == "__main__":
    unittest.main()
