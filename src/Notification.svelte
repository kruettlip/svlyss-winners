<script>
    import { Snackbar, Button } from "svelte-materialify";

    export let success = false;
    export let warning = false;
    export let error = false;
    export let active = false;
</script>

<Snackbar
    class="{success ? 'green justify-space-between darken-4' : 
            error ? 'red justify-space-between darken-1' : 
            warning ? 'orange justify-space-between lighten-3' : 'blue justify-space-between lighten-3'}"
    bind:active
    right
    top
    timeout={3000}
>
<slot></slot>
    <Button
        text
        on:click={() => {
            active = false;
        }}
    >
        x
    </Button>
</Snackbar>
