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
    import { sessionKey, currentMonth, apiURL, apiData } from "./store.js";
    import { onMount } from "svelte";
    import Notification from "./Notification.svelte";

    onMount(() => {
        if ($sessionKey) {
            fetch(`${$apiURL}/auth`, {
                method: "POST",
                body: JSON.stringify({
                    sessionKey: $sessionKey,
                }),
            })
                .then((response) => response.text())
                .then((data) => {
                    if (data != "") {
                        sessionKey.set(data);
                        loggedIn = true;
                    }
                })
                .catch((err) => {
                    error = true;
                    errorText = err.message;
                    loggedIn = false;
                    return [];
                });
        }

        fetch(`${$apiURL}/all`)
            .then((response) => response.json())
            .then((data) => {
                apiData.set(data);
                players = $currentMonth;
            })
            .catch((err) => {
                error = true;
                errorText = err.message;
                return [];
            });
    });

    const monthString = new Date().toLocaleString("de", { month: "long" });

    let show = false;
    let loggedIn = false;
    let username = "";
    let password = "";
    let savedSuccessfully = false;
    let error = false;
    let errorText = "";

    let players = $currentMonth;

    function increment(playerId) {
        let player = players.find((p) => p.id === playerId);
        if (player) {
            players[players.indexOf(player)].points += 1;
        }
    }

    function decrement(playerId) {
        let player = players.find((p) => p.id === playerId);
        if (player) {
            players[players.indexOf(player)].points -= 1;
        }
    }

    function tryLogin() {
        fetch(`${$apiURL}/login`, {
            method: "POST",
            body: JSON.stringify({
                username,
                password,
            }),
        })
            .then((response) => {
                if (response.status === 403)
                    throw new Error("Falsche Login-Daten");
                return response.text();
            })
            .then((data) => {
                if (data != "") {
                    sessionKey.set(data);
                    loggedIn = true;
                }
            })
            .catch((err) => {
                error = true;
                errorText = err.message;
                return [];
            });
    }

    function save() {
        fetch(`${$apiURL}/update`, {
            method: "POST",
            body: JSON.stringify({
                sessionKey: $sessionKey,
                players: players,
            }),
        })
            .then((response) => {
                if (response.status === 403)
                    throw new Error("Falsche Login-Daten");
                savedSuccessfully = true;
            })
            .catch((err) => {
                error = true;
                errorText = err.message;
                return [];
            });
    }

    function onKeyDown(e) {
        switch (e.keyCode) {
            case 13:
                tryLogin();
                break;
            default:
                break;
        }
    }
</script>

<Notification error bind:active={error}>{errorText}</Notification>
{#if loggedIn}
    <h4>Aktueller Monat: {monthString}</h4>
    <DataTable>
        <DataTableHead>
            <DataTableRow>
                <DataTableCell>Name</DataTableCell>
                <DataTableCell numeric>Punkte</DataTableCell>
            </DataTableRow>
        </DataTableHead>
        <DataTableBody>
            {#each players as player}
                <DataTableRow>
                    <DataTableCell>{player.name}</DataTableCell>
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
    <Notification success bind:active={savedSuccessfully}
        >Erfolgreich gespeichert.</Notification
    >
{:else}
    <div class="login-form" on:keydown={onKeyDown}>
        <Row>
            <Col class="flex-col">
                <h4 class="full-width">Login</h4>
                <TextField
                    dense
                    rounded
                    outlined
                    bind:value={username}
                    class="full-width"
                >
                    Benutzername
                </TextField>
                <TextField
                    type={show ? "text" : "password"}
                    dense
                    rounded
                    outlined
                    bind:value={password}
                    class="full-width"
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
        max-width: 90vw;
        padding: 30px;
    }
    :global(.flex-col) {
        display: flex;
        flex-direction: column;
        gap: 15px;
        align-items: flex-end;
    }
    :global(.login-button) {
        width: 100px;
    }
    :global(.save-button) {
        margin-top: 20px;
        width: 120px;
    }
    :global(.full-width) {
        width: 100%;
    }
    :global(th.s-tbl-cell) {
        text-align: left !important;
    }
</style>
