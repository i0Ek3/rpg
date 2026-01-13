/**
 * RPG: Random Password Generator - Core Logic
 * Mirrored from the Python backend in app.py
 */

const SPEC_STR = "!@#$%&*";
const CHOICE_LET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
const CHOICE_DIG = "0123456789";
const CHOICE_MIX = CHOICE_LET + CHOICE_DIG;

/**
 * Generate a random choice from a string
 * @param {string} str 
 * @returns {string}
 */
function randomChoice(str) {
    return str.charAt(Math.floor(Math.random() * str.length));
}

/**
 * Generate password with letters, digits, and special characters
 * Ensures at least 2 special characters and no special characters at the beginning or end.
 * @param {number} length 
 * @returns {string}
 */
function generateComplexPassword(length) {
    // 0 and -1 positions use CHOICE_MIX
    let first = randomChoice(CHOICE_MIX);
    let last = randomChoice(CHOICE_MIX);

    // Middle part can be mixed + special
    let middleLen = length - 2;
    let chars = CHOICE_MIX + SPEC_STR;
    let middle = [];
    for (let i = 0; i < middleLen; i++) {
        middle.push(randomChoice(chars));
    }

    // Ensure at least 2 special characters
    let currentSpecials = middle.filter(char => SPEC_STR.includes(char)).length;
    while (currentSpecials < 2) {
        // Find indices of non-special characters
        let nonSpecIndices = [];
        for (let i = 0; i < middle.length; i++) {
            if (!SPEC_STR.includes(middle[i])) {
                nonSpecIndices.push(i);
            }
        }

        if (nonSpecIndices.length === 0) break;

        let idx = nonSpecIndices[Math.floor(Math.random() * nonSpecIndices.length)];
        middle[idx] = randomChoice(SPEC_STR);
        currentSpecials++;
    }

    return first + middle.join('') + last;
}

/**
 * Generate password based on character set
 * @param {string} choiceSet 
 * @param {number} length 
 * @returns {string}
 */
function generatePasswordBy(choiceSet, length) {
    let pwd = "";
    for (let i = 0; i < length; i++) {
        pwd += randomChoice(choiceSet);
    }
    return pwd;
}

/**
 * Main function to generate all password groups
 * @param {number} length 
 * @returns {Array} Array of objects containing group name and passwords
 */
function generateAllGroups(length = 16) {
    if (length < 8) length = 8;
    if (length > 20) length = 20;

    return [
        {
            name: "Letters/Numbers/Special Characters",
            passwords: Array.from({ length: 5 }, () => generateComplexPassword(length))
        },
        {
            name: "Letters/Numbers",
            passwords: Array.from({ length: 5 }, () => generatePasswordBy(CHOICE_MIX, length))
        },
        {
            name: "Numbers",
            passwords: Array.from({ length: 5 }, () => generatePasswordBy(CHOICE_DIG, length))
        },
        {
            name: "Letters",
            passwords: Array.from({ length: 5 }, () => generatePasswordBy(CHOICE_LET, length))
        }
    ];
}

// Export for test if needed (browser will use it as global if not exported)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { generateAllGroups, generateComplexPassword, generatePasswordBy };
}
