<script>
    import {
        Tabs,
        Tab,
        Window,
        WindowItem,
        DataTable,
        DataTableHead,
        DataTableRow,
        DataTableCell,
        DataTableBody,
    } from "svelte-materialify";
    import { onMount } from "svelte";

    import { firstRound, secondRound, apiURL, apiData } from "./store.js";
    import Notification from "./Notification.svelte";

    let selectedTab = 0;
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
</script>

<Tabs class="indigo-text" bind:value={selectedTab} fixedTabs>
    <div slot="tabs">
        <Tab>Vorrunde</Tab>
        <Tab>Rückrunde</Tab>
    </div>
</Tabs>

<Window value={selectedTab} class="ma-4">
    <WindowItem>
        <DataTable>
            <DataTableHead>
                <DataTableRow>
                    <DataTableCell numeric>Rang</DataTableCell>
                    <DataTableCell>Name</DataTableCell>
                    <DataTableCell numeric>Punkte</DataTableCell>
                </DataTableRow>
            </DataTableHead>
            <DataTableBody>
                {#each $firstRound as player, index}
                    <DataTableRow>
                        <DataTableCell numeric>{index + 1}</DataTableCell>
                        <DataTableCell>{player.name}</DataTableCell>
                        <DataTableCell numeric>{player.points}</DataTableCell>
                    </DataTableRow>
                {/each}
            </DataTableBody>
        </DataTable>
    </WindowItem>
    <WindowItem>
        <DataTable>
            <DataTableHead>
                <DataTableRow>
                    <DataTableCell numeric>Rang</DataTableCell>
                    <DataTableCell>Name</DataTableCell>
                    <DataTableCell numeric>Punkte</DataTableCell>
                </DataTableRow>
            </DataTableHead>
            <DataTableBody>
                {#each $secondRound as player, index}
                    <DataTableRow>
                        <DataTableCell numeric>{index + 1}</DataTableCell>
                        <DataTableCell>{player.name}</DataTableCell>
                        <DataTableCell numeric>{player.points}</DataTableCell>
                    </DataTableRow>
                {/each}
            </DataTableBody>
        </DataTable>
    </WindowItem>
</Window>
<Notification error bind:active={error}>{errorText}</Notification>
