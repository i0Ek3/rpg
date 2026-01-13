document.addEventListener('DOMContentLoaded', function () {
    const generateBtn = document.getElementById('generate-btn');
    const lengthInput = document.getElementById('length');
    const passwordContainer = document.getElementById('password-container');

    // Create toast element
    const toast = document.createElement('div');
    toast.className = 'copy-toast';
    toast.textContent = 'Password Copied!';
    document.body.appendChild(toast);

    function showToast() {
        toast.classList.add('show');
        setTimeout(() => {
            toast.classList.remove('show');
        }, 2000);
    }

    function renderPasswords() {
        const length = parseInt(lengthInput.value) || 16;
        const groups = generateAllGroups(length);

        passwordContainer.innerHTML = '';

        groups.forEach(group => {
            const groupDiv = document.createElement('div');
            groupDiv.className = 'password-group';

            const groupName = document.createElement('div');
            groupName.className = 'group-name';
            groupName.textContent = group.name;
            groupDiv.appendChild(groupName);

            const listDiv = document.createElement('div');
            listDiv.className = 'password-list';

            group.passwords.forEach(pwd => {
                const item = document.createElement('div');
                item.className = 'password-item';
                item.textContent = pwd;
                item.addEventListener('click', () => {
                    copyToClipboard(pwd);
                });
                listDiv.appendChild(item);
            });

            groupDiv.appendChild(listDiv);
            passwordContainer.appendChild(groupDiv);
        });
    }

    function copyToClipboard(text) {
        navigator.clipboard.writeText(text).then(() => {
            showToast();
        }).catch(err => {
            console.error('Failed to copy: ', err);
            // Fallback for older browsers or restricted environments
            const textArea = document.createElement("textarea");
            textArea.value = text;
            document.body.appendChild(textArea);
            textArea.select();
            try {
                document.execCommand('copy');
                showToast();
            } catch (err) {
                console.error('Fallback copy failed', err);
            }
            document.body.removeChild(textArea);
        });
    }

    generateBtn.addEventListener('click', renderPasswords);

    // Initial generate
    renderPasswords();
});
