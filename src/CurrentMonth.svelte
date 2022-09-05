<script>
    import {
        DataTable,
        DataTableHead,
        DataTableRow,
        DataTableCell,
        DataTableBody,
    } from "svelte-materialify";
    import { onMount } from "svelte";
    import { currentMonth, apiData, apiURL } from "./store.js";
    import Notification from "./Notification.svelte";

    let error = false;
    let errorText = "";

    onMount(() => {
        fetch(`${$apiURL}/all`)
            .then((response) => response.json())
            .then((data) => {
                apiData.set(data);
            })
            .catch((err) => {
                error = true;
                errorText = err.message;
                return [];
            });
    });

    const monthString = new Date().toLocaleString("de", { month: "long" });
</script>

<h4>Aktueller Monat: {monthString}</h4>

<DataTable>
    <DataTableHead>
        <DataTableRow>
            <DataTableCell numeric>Rang</DataTableCell>
            <DataTableCell>Name</DataTableCell>
            <DataTableCell numeric>Punkte</DataTableCell>
        </DataTableRow>
    </DataTableHead>
    <DataTableBody>
        {#each $currentMonth as player, index}
            <DataTableRow>
                <DataTableCell numeric>{index + 1}</DataTableCell>
                <DataTableCell>{player.name}</DataTableCell>
                <DataTableCell numeric>{player.points}</DataTableCell>
            </DataTableRow>
        {/each}
    </DataTableBody>
</DataTable>
<Notification error bind:active={error}>{errorText}</Notification>

<style>
    h4 {
        margin-bottom: 20px;
    }
    :global(.s-tbl-cell) {
        height: 40px !important;
    }
</style>
