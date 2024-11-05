import numpy as np

def generate_random_data(mean, variance, num_samples):
    low = max(mean - variance, 0)
    high = min(mean + variance + 1, 90)

    if low >= high:
        high = low + 1

    return np.random.randint(low, high, num_samples)


def calculate_aggregated_score(departments):
    total_score = 0
    total_importance = 0

    for name, users, importance in departments:
        department_score = np.mean(users)
        total_score += department_score * importance
        total_importance += importance

    if total_importance > 0:
        return total_score / total_importance
    return 0

import unittest


class TestCyberSecurityAggregation(unittest.TestCase):

    def test_single_department(self):
        users = generate_random_data(50, 10, 5)
        department = ("Инжиниринг", users, 3)
        departments = [department]
        aggregated_score = calculate_aggregated_score(departments)
        self.assertTrue(0 <= aggregated_score <= 90, "Агрегированный балл выходит за пределы диапазона.")

    def test_multiple_departments_equal_importance(self):
        dept1_users = generate_random_data(45, 5, 10)
        dept2_users = generate_random_data(50, 5, 10)
        dept3_users = generate_random_data(55, 5, 10)
        departments = [
            ("Инжиниринг", dept1_users, 3),
            ("Маркетинг", dept2_users, 3),
            ("Финансы", dept3_users, 3)
        ]

        aggregated_score = calculate_aggregated_score(departments)
        self.assertTrue(0 <= aggregated_score <= 90, "Агрегированный балл выходит за пределы диапазона.")

    def test_multiple_departments_varying_importance(self):
        dept1_users = generate_random_data(40, 5, 20)
        dept2_users = generate_random_data(60, 5, 10)
        dept3_users = generate_random_data(70, 5, 15)
        departments = [
            ("Инжиниринг", dept1_users, 2),  # Важность 2
            ("Маркетинг", dept2_users, 5),  # Важность 5
            ("Финансы", dept3_users, 3)  # Важность 3
        ]

        aggregated_score = calculate_aggregated_score(departments)
        self.assertTrue(0 <= aggregated_score <= 90, "Агрегированный балл выходит за пределы диапазона.")

    def test_extreme_cases(self):
        dept1_users = generate_random_data(5, 5, 10)
        dept2_users = generate_random_data(85, 5, 10)
        dept3_users = generate_random_data(90, 1, 10)
        departments = [
            ("HR", dept1_users, 1),
            ("Инжиниринг", dept2_users, 5),
            ("Финансы", dept3_users, 3)
        ]

        aggregated_score = calculate_aggregated_score(departments)
        self.assertTrue(0 <= aggregated_score <= 90, "Агрегированный балл выходит за пределы диапазона.")


if __name__ == "__main__":
    unittest.main()
