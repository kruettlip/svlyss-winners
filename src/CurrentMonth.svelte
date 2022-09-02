<script>
    import {
        DataTable,
        DataTableHead,
        DataTableRow,
        DataTableCell,
        DataTableBody,
    } from "svelte-materialify";
    import { onMount } from "svelte";
    import { currentMonth, apiData } from "./store.js";

    onMount(async () => {
        fetch(
            "http://localhost:5000/api/all"
        )
            .then((response) => response.json())
            .then((data) => {
                apiData.set(data);
            })
            .catch((error) => {
                console.log(error);
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
            <DataTableCell>Vorname</DataTableCell>
            <DataTableCell>Nachname</DataTableCell>
            <DataTableCell numeric>Punkte</DataTableCell>
        </DataTableRow>
    </DataTableHead>
    <DataTableBody>
        {#each $currentMonth as player, index}
            <DataTableRow>
                <DataTableCell numeric>{index + 1}</DataTableCell>
                <DataTableCell>{player.firstname}</DataTableCell>
                <DataTableCell>{player.lastname}</DataTableCell>
                <DataTableCell numeric>{player.points}</DataTableCell>
            </DataTableRow>
        {/each}
    </DataTableBody>
</DataTable>

<style>
    h4 {
        margin-bottom: 20px;
    }
</style>
