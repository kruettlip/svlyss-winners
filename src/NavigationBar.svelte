<script>
    import {
        AppBar,
        Button,
        Icon,
        NavigationDrawer,
        Overlay,
        List,
        ListItemGroup,
        ListItem,
    } from "svelte-materialify";
    import { mdiMenu, mdiInvertColors, mdiCalendarToday, mdiFormatListNumbered, mdiAccountKey } from "@mdi/js";
    import { createEventDispatcher } from "svelte";
    import { Link } from "svelte-navigator";

    const dispatch = createEventDispatcher();

    let active = false;
    
    const navItems = [
    { text: 'Aktueller Monat', icon: mdiCalendarToday, path: '/' },
    { text: 'Gesamtübersicht', icon: mdiFormatListNumbered, path: '/overview' },
    { text: 'Admin', icon: mdiAccountKey, path: '/admin' },
  ];

    function toggleNavigation() {
        active = !active;
    }

    function toggleTheme() {
        dispatch("toggleTheme");
    }
</script>

<div style="height:80px">
    <AppBar class="indigo darken-4">
        <div slot="icon">
            <Button
                fab
                depressed
                on:click={toggleNavigation}
                class="indigo darken-4">
                <Icon path={mdiMenu} class="white-text" />
            </Button>
        </div>
        <span slot="title" class="white-text">
            Zwöi - Rangliste
        </span>
        <Button on:click={toggleTheme} icon class="white-text right">
            <Icon path={mdiInvertColors} />
        </Button>
    </AppBar>
    <NavigationDrawer style="position: relative" {active}>
        <List nav dense>
            <ListItemGroup>
              {#each navItems as item}
                <Link to={item.path} on:click={toggleNavigation}>
                    <ListItem>
                    <span slot="prepend">
                        <Icon path={item.icon} />
                    </span>
                    {item.text}
                    </ListItem>
                </Link>
              {/each}
            </ListItemGroup>
          </List>
    </NavigationDrawer>
    <Overlay {active} absolute on:click={toggleNavigation} index={1} />
</div>

<style>
    :global(.right) {
        position: absolute !important;
        right: 10px;
    }
    :global(button) {
        margin: 0;
    }
    :global(.s-overlay), :global(.s-navigation-drawer) {
        height: 100vh !important;
    }
    :global(AppBar) {
        margin-bottom: -10px;
    }
</style>