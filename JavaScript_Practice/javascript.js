// Задание 1: Вывести в консоль приветствие
console.log("Привет, мир!");

// Задание 2: Создать переменные и выполнить операции с ними
let a = 5;
let b = 10;
let sum = a + b;
let product = a * b;
console.log("Сумма:", sum);
console.log("Произведение:", product);

// Задание 3: Создать функцию для вычисления суммы двух чисел
function calculateSum(num1, num2) {
  return num1 + num2;
}
let result = calculateSum(3, 7);
console.log("Результат:", result);

// Задание 4: Создать массив и выполнить операции с ним
let numbers = [1, 2, 3, 4, 5];
console.log("Длина массива:", numbers.length);
console.log("Первый элемент:", numbers[0]);
console.log("Последний элемент:", numbers[numbers.length - 1]);

// Задание 5: Создать объект и получить доступ к его свойствам
let person = {
  name: "John",
  age: 30,
  city: "New York"
};
console.log("Имя:", person.name);
console.log("Возраст:", person.age);
console.log("Город:", person.city);

// Задание 6: Создать функцию для определения четности числа
function isEven(number) {
    if (number % 2 === 0) {
      return true;
    } else {
      return false;
    }
  }
  console.log(isEven(4)); // Ожидаемый результат: true
  console.log(isEven(7)); // Ожидаемый результат: false
  
  // Задание 7: Создать функцию для поиска максимального числа в массиве
  function findMaxNumber(numbers) {
    let max = numbers[0];
    for (let i = 1; i < numbers.length; i++) {
      if (numbers[i] > max) {
        max = numbers[i];
      }
    }
    return max;
  }
  console.log(findMaxNumber([5, 2, 9, 1, 7])); // Ожидаемый результат: 9
  
  // Задание 8: Создать функцию для проверки наличия элемента в массиве
  function containsElement(array, element) {
    for (let i = 0; i < array.length; i++) {
      if (array[i] === element) {
        return true;
      }
    }
    return false;
  }
  console.log(containsElement([1, 3, 5, 7, 9], 5)); // Ожидаемый результат: true
  console.log(containsElement([2, 4, 6, 8, 10], 3)); // Ожидаемый результат: false
  
  // Задание 9: Создать функцию для объединения двух массивов
  function mergeArrays(array1, array2) {
    return array1.concat(array2);
  }
  console.log(mergeArrays([1, 2, 3], [4, 5, 6])); // Ожидаемый результат: [1, 2, 3, 4, 5, 6]
  
  // Задание 10: Создать функцию для перевода строки в верхний регистр
  function convertToUpperCase(string) {
    return string.toUpperCase();
  }
  console.log(convertToUpperCase("hello")); // Ожидаемый результат: "HELLO"
  

// Задание 11: Создать функцию для проверки является ли число простым
function isPrime(number) {
    if (number <= 1) {
      return false;
    }
    for (let i = 2; i <= Math.sqrt(number); i++) {
      if (number % i === 0) {
        return false;
      }
    }
    return true;
  }
  console.log(isPrime(7)); // Ожидаемый результат: true
  console.log(isPrime(12)); // Ожидаемый результат: false
  
  // Задание 12: Создать функцию для сортировки массива чисел по возрастанию
  function sortNumbers(numbers) {
    return numbers.sort((a, b) => a - b);
  }
  console.log(sortNumbers([5, 2, 9, 1, 7])); // Ожидаемый результат: [1, 2, 5, 7, 9]
  
  // Задание 13: Создать функцию для подсчета факториала числа
  function factorial(number) {
    if (number === 0 || number === 1) {
      return 1;
    }
    return number * factorial(number - 1);
  }
  console.log(factorial(5)); // Ожидаемый результат: 120
  
  // Задание 14: Создать функцию для проверки является ли строка палиндромом
  function isPalindrome(string) {
    const reversedString = string.split("").reverse().join("");
    return string === reversedString;
  }
  console.log(isPalindrome("level")); // Ожидаемый результат: true
  console.log(isPalindrome("hello")); // Ожидаемый результат: false
  
  // Задание 15: Создать функцию для генерации случайного числа в заданном диапазоне
  function generateRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }
  console.log(generateRandomNumber(1, 10)); // Ожидаемый результат: случайное число от 1 до 10
  
// Задание 16: Создать функцию для поиска наиболее часто встречающегося элемента в массиве
function findMostFrequentElement(array) {
    let frequencyMap = {};
    let maxFrequency = 0;
    let mostFrequentElement;
  
    for (let element of array) {
      if (frequencyMap[element]) {
        frequencyMap[element]++;
      } else {
        frequencyMap[element] = 1;
      }
  
      if (frequencyMap[element] > maxFrequency) {
        maxFrequency = frequencyMap[element];
        mostFrequentElement = element;
      }
    }
  
    return mostFrequentElement;
  }
  console.log(findMostFrequentElement([1, 2, 3, 2, 4, 2, 5])); // Ожидаемый результат: 2
  
  // Задание 17: Создать функцию для проверки является ли число палиндромом
  function isPalindromeNumber(number) {
    const reversedNumber = parseInt(number.toString().split("").reverse().join(""));
    return number === reversedNumber;
  }
  console.log(isPalindromeNumber(12321)); // Ожидаемый результат: true
  console.log(isPalindromeNumber(12345)); // Ожидаемый результат: false
  
  // Задание 18: Создать функцию для суммирования всех простых чисел до заданного числа
  function sumOfPrimes(limit) {
    let sum = 0;
  
    for (let number = 2; number <= limit; number++) {
      if (isPrime(number)) {
        sum += number;
      }
    }
  
    return sum;
  }
  console.log(sumOfPrimes(10)); // Ожидаемый результат: 17 (2 + 3 + 5 + 7)
  
  // Задание 19: Создать функцию для проверки является ли число совершенным
  function isPerfectNumber(number) {
    let sum = 0;
  
    for (let i = 1; i < number; i++) {
      if (number % i === 0) {
        sum += i;
      }
    }
  
    return sum === number;
  }
  console.log(isPerfectNumber(28)); // Ожидаемый результат: true
  console.log(isPerfectNumber(12)); // Ожидаемый результат: false
  
  // Задание 20: Создать функцию для генерации уникального идентификатора
  function generateUniqueId() {
    return Date.now().toString(36) + Math.random().toString(36).substr(2, 5);
  }
  console.log(generateUniqueId()); // Ожидаемый результат: уникальный идентификатор
  