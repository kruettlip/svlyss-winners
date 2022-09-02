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

    import { firstRound, secondRound } from './store.js'

    let selectedTab = 0;
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
                    <DataTableCell>Vorname</DataTableCell>
                    <DataTableCell>Nachname</DataTableCell>
                    <DataTableCell numeric>Punkte</DataTableCell>
                </DataTableRow>
            </DataTableHead>
            <DataTableBody>
                {#each $firstRound as player, index}
                    <DataTableRow>
                        <DataTableCell numeric>{index + 1}</DataTableCell>
                        <DataTableCell>{player.firstname}</DataTableCell>
                        <DataTableCell>{player.lastname}</DataTableCell>
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
                    <DataTableCell>Vorname</DataTableCell>
                    <DataTableCell>Nachname</DataTableCell>
                    <DataTableCell numeric>Punkte</DataTableCell>
                </DataTableRow>
            </DataTableHead>
            <DataTableBody>
                {#each $secondRound as player, index}
                    <DataTableRow>
                        <DataTableCell numeric>{index + 1}</DataTableCell>
                        <DataTableCell>{player.firstname}</DataTableCell>
                        <DataTableCell>{player.lastname}</DataTableCell>
                        <DataTableCell numeric>{player.points}</DataTableCell>
                    </DataTableRow>
                {/each}
            </DataTableBody>
        </DataTable>
    </WindowItem>
</Window>
