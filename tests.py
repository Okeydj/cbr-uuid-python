from unittest import TestCase
import uuid_cbr


class UuidCbrTestCase(TestCase):
    def test_uuid_cbr(self):
        self.assertEqual(len(uuid_cbr.uuid()), len('279c0330-2c4a-11eb-80f4-1ff63512f756-0'))

    def test_generate_load(self):
        generated_count = 1
        max_count = 100000
        for x in range(1, max_count):
            try:
                uuid_cbr.uuid()
                generated_count += 1
            except RuntimeError:
                pass
        self.assertEqual(generated_count, max_count)
