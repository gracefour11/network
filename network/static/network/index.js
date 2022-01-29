function edit_post(id) {
    const post_body = document.querySelector(`#post_body_${id}`);
    post_body.style.display = 'none';

    const edit_post_view = document.querySelector(`#edit_post_body_${id}`);
    edit_post_view.style.display = 'block';

    const edit_form = document.querySelector(`#edit_form_${id}`);
    edit_form.onsubmit = () => {
        fetch(`/edit/${id}`, {
            method: 'POST',
            body: JSON.stringify({
                body: document.querySelector(`#edit_text_${id}`).value
            })
        })
        .then(() => {
            post_body.innerHTML = body
            edit_post_view.style.display = 'none'
            post_body.style.display = 'block'
        })
    }
}

