<?php

namespace MauticPlugin\MauticBeefreeBundle\Controller;

use Mautic\CoreBundle\Controller\CommonController;
use MauticPlugin\MauticBeefreeBundle\Entity\BeefreeTheme;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;

class BeefreeDeleteThemeController extends CommonController
{
    public function deleteThemeAction(Request $request): JsonResponse
    {
        // set header
        header('Access-Control-Allow-Origin: *');

        // get data (if POST)
        $data = json_decode($request->getContent());
        $id = $data->id;

        // get bfrepo
        $bfrepo = $this->getDoctrine()->getRepository(BeefreeTheme::class);

        // delete new theme
        $bfrepo->deleteBeefreeTheme($id);

        // create response
        $response = new JsonResponse([
            'success' => true,
        ]);

        // set header
        $response->headers->set('Content-Type', 'application/json');
        $response->headers->set('Access-Control-Allow-Origin', '*');

        return $response;
    }
}