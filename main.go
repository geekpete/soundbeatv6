package main

import (
	"os"

	"github.com/geekpete/soundbeat6/cmd"
)

func main() {
	if err := cmd.RootCmd.Execute(); err != nil {
		os.Exit(1)
	}
}
