<script>
    import {
        TextField,
        Row,
        Col,
        Icon,
        Button,
        DataTable,
        DataTableHead,
        DataTableRow,
        DataTableCell,
        DataTableBody,
    } from "svelte-materialify";
    import { mdiEyeOff, mdiEye, mdiPlus, mdiMinus } from "@mdi/js";
    import { sessionKey, currentMonth, apiURL } from "./store.js";
    import { onMount } from "svelte";

    onMount(async () => {
        if (sessionKey !== "") {
            await fetch(`${$apiURL}/auth`, {
                method: "POST",
                body: JSON.stringify({
                    sessionKey: $sessionKey,
                }),
            })
                .then((response) => response.text())
                .then((data) => {
                    if (data != "") {
                        loggedIn = true;
                    }
                })
                .catch((error) => {
                    console.log(error);
                    loggedIn = false;
                    return [];
                });
        }
    });

    const monthString = new Date().toLocaleString("de", { month: "long" });

    let show = false;
    let loggedIn = false;
    let username = "";
    let password = "";

    const players = $currentMonth;

    function increment(playerId) {
        players[playerId - 1].points += 1;
    }

    function decrement(playerId) {
        players[playerId - 1].points -= 1;
    }

    async function tryLogin() {
        await fetch(`${$apiURL}/login`, {
            method: "POST",
            body: JSON.stringify({
                username,
                password,
            }),
        })
            .then((response) => response.text())
            .then((data) => {
                sessionKey.set(data);
                loggedIn = true;
            })
            .catch((error) => {
                console.log(error);
                return [];
            });
    }

    async function save() {
        console.log(players);
        await fetch(`${$apiURL}/update`, {
            method: "POST",
            body: JSON.stringify({
                sessionKey: $sessionKey,
                players: players,
            }),
        })
            .then((response) => response.json())
            .catch((error) => {
                console.log(error);
                return [];
            });
    }
</script>

{#if loggedIn}
    <h4>Aktueller Monat: {monthString}</h4>
    <DataTable>
        <DataTableHead>
            <DataTableRow>
                <DataTableCell>Vorname</DataTableCell>
                <DataTableCell>Nachname</DataTableCell>
                <DataTableCell numeric>Punkte</DataTableCell>
            </DataTableRow>
        </DataTableHead>
        <DataTableBody>
            {#each players as player}
                <DataTableRow>
                    <DataTableCell>{player.firstname}</DataTableCell>
                    <DataTableCell>{player.lastname}</DataTableCell>
                    <DataTableCell numeric>
                        <Button
                            fab
                            size="small"
                            on:click={increment(player.id)}
                        >
                            <Icon path={mdiPlus} />
                        </Button>
                        {player.points}
                        <Button
                            fab
                            size="small"
                            on:click={decrement(player.id)}
                        >
                            <Icon path={mdiMinus} />
                        </Button>
                    </DataTableCell>
                </DataTableRow>
            {/each}
        </DataTableBody>
    </DataTable>
    <br />
    <Button rounded class="indigo darken-4 save-button" on:click={save}>
        <span class="white-text">Speichern</span>
    </Button>
{:else}
    <div class="login-form">
        <Row>
            <Col>
                <h4 class="title">Login</h4>
                <TextField dense rounded outlined bind:value={username}
                    >Benutzername</TextField
                >
                <br />
                <TextField
                    type={show ? "text" : "password"}
                    dense
                    rounded
                    outlined
                    bind:value={password}
                >
                    Passwort
                    <div
                        slot="append"
                        on:click={() => {
                            show = !show;
                        }}
                    >
                        <Icon path={show ? mdiEyeOff : mdiEye} />
                    </div>
                </TextField>
                <br />
                <Button
                    rounded
                    class="indigo darken-4 login-button"
                    on:click={tryLogin}
                >
                    <span class="white-text">Login</span>
                </Button>
            </Col>
        </Row>
    </div>
{/if}

<style>
    .login-form {
        border: solid 1px darkgray;
        border-radius: 10px;
        max-width: 500px;
        padding: 30px;
    }
    :global(.login-button) {
        width: 100px;
        position: relative;
        left: 335px;
    }
    :global(.save-button) {
        margin-top: 20px;
        width: 120px;
    }
    .title {
        margin-bottom: 30px;
    }
    h4 {
        margin-bottom: 20px;
    }
</style>
