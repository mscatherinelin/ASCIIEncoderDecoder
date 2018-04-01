import unittest
from ASCIIEncoderDecoder import ASCIIFormatTransporter


class EncodeTests(unittest.TestCase):
    def testEncodeEmpty(self):
        test = ('TestCases/empty.txt', '', '')
        result = ASCIIFormatTransporter(test[0], False)
        self.assertEqual(result.data, test[1])
        self.assertFalse(result.alreadyEncoded)

        result.encode()

        self.assertTrue(result.alreadyEncoded)
        self.assertEqual(result.data, test[2])

    def testEncode(self):
        tests = [
            ('TestCases/test1.txt', 'aabb', '2a 2b'),
            ('TestCases/newline.txt', 'aaa\nbbb', '3a 1\n 3b'),
            ('TestCases/spaces.txt', '    333   999', '4  33 3  39')
        ]
        for file, fileContent, result in tests:
            obj = ASCIIFormatTransporter(file, False)
            self.assertEqual(obj.data, fileContent)
            self.assertFalse(obj.alreadyEncoded)

            obj.encode()

            self.assertEqual(obj.data, result)
            self.assertTrue(obj.alreadyEncoded)

    def testAlreadyEncodedFile(self):
        test = ('TestCases/test1.txt', 'aabb', '2a 2b')
        result = ASCIIFormatTransporter(test[0], False)
        self.assertEqual(result.data, test[1])
        self.assertFalse(result.alreadyEncoded)
        result.encode()

        self.assertRaises(ValueError, lambda: result.encode())


class DecodeTests(unittest.TestCase):
    def testDecodeEmpty(self):
        test = ('TestCases/empty.txt', '', '')
        result = ASCIIFormatTransporter(test[0], False)
        self.assertEqual(result.data, test[1])
        self.assertFalse(result.alreadyEncoded)

        result.encode()

        self.assertTrue(result.alreadyEncoded)
        self.assertEqual(result.data, test[2])

        result.decode()

        self.assertEqual(result.data, test[1])
        self.assertFalse(result.alreadyEncoded)

    def testDecode(self):
        tests = [
            ('TestCases/test1.txt', 'aabb', '2a 2b'),
            ('TestCases/newline.txt', 'aaa\nbbb', '3a 1\n 3b'),
            ('TestCases/spaces.txt', '    333   999', '4  33 3  39')
        ]
        for file, fileContent, result in tests:
            obj = ASCIIFormatTransporter(file, False)
            self.assertEqual(obj.data, fileContent)
            self.assertFalse(obj.alreadyEncoded)

            obj.encode()

            self.assertEqual(obj.data, result)
            self.assertTrue(obj.alreadyEncoded)

            obj.decode()

            self.assertEqual(obj.data, fileContent)
            self.assertFalse(obj.alreadyEncoded)

    def testAlreadyDecodedFile(self):
        test = ('TestCases/test1.txt', 'aabb', '2a 2b')
        result = ASCIIFormatTransporter(test[0], False)
        self.assertEqual(result.data, test[1])
        self.assertFalse(result.alreadyEncoded)

        result.encode()

        self.assertTrue(result.alreadyEncoded)
        self.assertEqual(result.data, test[2])

        result.decode()

        self.assertEqual(result.data, test[1])
        self.assertFalse(result.alreadyEncoded)

        self.assertRaises(ValueError, lambda: result.decode())

class EncodeDecodeASCIIArt(unittest.TestCase):
    def testASCIIArt(self):
        tests = [
            'TestCases/data.txt'
        ]

        for file in tests:
            with open(file) as f:
                fileContent = f.read()
            object = ASCIIFormatTransporter(file, False)
            self.assertEqual(fileContent, object.data)
            self.assertFalse(object.alreadyEncoded)

            object.encode()
            self.assertTrue(object.alreadyEncoded)

            object.decode()
            self.assertEqual(object.data, fileContent)
            self.assertFalse(object.alreadyEncoded)




if __name__ == '__main__':
    unittest.main()
