const apiUrl = 'http://localhost:8000/api/user';

async function fetchAllUsers() {
    const response = await fetch(apiUrl);
    const users = await response.json();
    const userList = document.getElementById('users');
    userList.innerHTML = '';
    users.forEach(user => {
        const li = document.createElement('li');
        li.textContent = `ID: ${user.id}, Username: ${user.username}`;
        userList.appendChild(li);
    });
}

async function createUser() {
    const username = document.getElementById('username').value;
    const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username })
    });
    if (response.ok) {
        alert('User created successfully');
        fetchAllUsers();
    } else {
        alert('Failed to create user');
    }
}

async function editUser() {
    const userId = document.getElementById('edit-user-id').value;
    const newUsername = document.getElementById('edit-username').value;

    // Создаем объект с обновляемыми данными
    const updatedData = {};
    if (newUsername) updatedData.username = newUsername;

    const response = await fetch(`${apiUrl}/${userId}`, {
        method: 'PATCH', // Изменяем метод на PATCH
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(updatedData) // Отправляем только измененные данные
    });
    if (response.ok) {
        alert('User updated successfully');
        fetchAllUsers();
    } else {
        alert('Failed to update user');
    }
}


async function deleteUser() {
    const userId = document.getElementById('delete-user-id').value;
    const response = await fetch(`${apiUrl}/${userId}`, {
        method: 'DELETE'
    });
    if (response.ok) {
        alert('User deleted successfully');
        fetchAllUsers();
    } else {
        alert('Failed to delete user');
    }
}

async function searchUser() {
    const userId = document.getElementById('search-user-id').value;
    const response = await fetch(`${apiUrl}/${userId}`);
    const user = await response.json();
    const searchResult = document.getElementById('search-result');
    if (user) {
        searchResult.textContent = `ID: ${user.id}, Username: ${user.username}`;
    } else {
        searchResult.textContent = 'User not found';
    }
}

window.onload = fetchAllUsers;
